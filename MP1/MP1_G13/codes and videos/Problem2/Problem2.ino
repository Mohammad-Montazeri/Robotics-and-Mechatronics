#include "I2Cdev.h"
#include <Kalman.h>
#include "MPU6050_6Axis_MotionApps20.h"


#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
#include "Wire.h"
#endif

// uncomment "OUTPUT_READABLE_QUATERNION" if you want to see the actual
// quaternion components in a [w, x, y, z] format
//#define OUTPUT_READABLE_QUATERNION

// uncomment "OUTPUT_READABLE_YAWPITCHROLL" if you want to see the yaw/
// pitch/roll angles (in degrees) calculated from the quaternions coming
// from the FIFO.
#define OUTPUT_READABLE_YAWPITCHROLL

// Variables related to gyroscope data
bool dmpReady = false;
uint8_t devStatus;
uint8_t fifoBuffer[64];

Quaternion q;         // [w, x, y, z]         quaternion container
VectorFloat gravity;  // [x, y, z]            gravity vector
float ypr[3];         // [yaw, pitch, roll]   yaw/pitch/roll container and gravity vector

// Variables related to complementary filter data
int ax, ay, az;
int gx, gy, gz;

long tiempo_prev;
float dt;
float ang_x_prev, ang_y_prev;

// Variables related to kalman filter data
Kalman kalmanX;  // Create the Kalman instances
Kalman kalmanY;
int16_t tempRaw;

double compAngleX, compAngleY;  // Calculated angle using a complementary filter
double kalAngleX, kalAngleY;    // Calculated angle using a Kalman filter


const int mpuAddress = 0x68;  // It can be 0x68 or 0x69
MPU6050 mpu(mpuAddress);


void updateFiltered() {
  // Calculate the execution time of the function in each round
  dt = (micros() - tiempo_prev) / 1000000.0;
  tiempo_prev = micros();

  //Calculate the angles with accelerometer
  float roll = atan2(ay, az) * (180.0 / M_PI);
  float pitch = atan2(ax, az) * (180.0 / M_PI);

  double gyroXrate = gx / 131.0;  // Convert to deg/s
  double gyroYrate = gy / 131.0;  // Convert to deg/s
  double gyroZrate = gz / 131.0;  // Convert to deg/s

  if ((roll < -90 && kalAngleX > 90) || (roll > 90 && kalAngleX < -90)) {
    kalmanX.setAngle(roll);
    compAngleX = roll;
    kalAngleX = roll;
  } else {
    kalAngleX = kalmanX.getAngle(roll, gyroXrate, dt);  // Calculate the angle using a Kalman filter
  }

  if (abs(kalAngleX) > 90) {
    gyroYrate = -gyroYrate;  // Invert rate, so it fits the restriced accelerometer reading
  }
  kalAngleY = kalmanY.getAngle(pitch, gyroYrate, dt);

  // This fixes the transition problem when the accelerometer angle jumps between -180 and 180 degrees
  if ((pitch < -90 && kalAngleY > 90) || (pitch > 90 && kalAngleY < -90)) {
    kalmanY.setAngle(pitch);
    compAngleY = pitch;
    kalAngleY = pitch;
  } else {
    kalAngleY = kalmanY.getAngle(pitch, gyroYrate, dt);  // Calculate the angle using a Kalman filter
  }

  if (abs(kalAngleY) > 90) {
    gyroXrate = -gyroXrate;  // Invert rate, so it fits the restriced accelerometer reading
  }
  kalAngleX = kalmanX.getAngle(roll, gyroXrate, dt);  // Calculate the angle using a Kalman filter

  //Calculate rotation angle with gyroscope and complementary filter
  compAngleX = 0.80 * (ang_x_prev + gyroXrate * dt) + 0.20 * roll;
  compAngleY = 0.80 * (ang_y_prev + gyroYrate * dt) + 0.20 * pitch;

  ang_x_prev = compAngleX;
  ang_y_prev = compAngleY;
}


void setup() {

  delay(1000);  // Wait for sensor to stabilize
  Serial.begin(115200);
  Wire.begin();
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
  Wire.setClock(400000);
#elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
  Fastwire::setup(400, true);
#endif

  while (!Serial)
    ;

  Serial.println(F("Initializing I2C devices..."));
  mpu.initialize();

  Serial.println(F("Testing device connections..."));
  Serial.println(mpu.testConnection() ? F("MPU6050 connection successful") : F("MPU6050 connection failed"));

  Serial.println(F("Initializing DMP..."));
  devStatus = mpu.dmpInitialize();
  /*
  mpu.setXGyroOffset(220);
  mpu.setYGyroOffset(76);
  mpu.setZGyroOffset(-85);
  mpu.setZAccelOffset(1788); 
  */
  if (devStatus == 0) {
    /*
    mpu.CalibrateAccel(6);
    mpu.CalibrateGyro(6);
    mpu.PrintActiveOffsets();
    */
    Serial.println(F("Enabling DMP..."));
    mpu.setDMPEnabled(true);
    dmpReady = true;
  } else {
    Serial.print(F("DMP Initialization failed (code "));
    Serial.print(devStatus);
    Serial.println(F(")"));
  }

  // complementary and kalman filter
  mpu.initialize();
  // calculate roll and pitch angle as primary data
  float roll = atan2(mpu.getAccelerationY(), mpu.getAccelerationZ()) * (180.0 / M_PI);
  float pitch = atan2(mpu.getAccelerationX(), mpu.getAccelerationZ()) * (180.0 / M_PI);
  // Set starting angle
  kalmanX.setAngle(roll);
  kalmanY.setAngle(pitch);
  ang_x_prev = roll;
  ang_y_prev = pitch;
}

void loop() {
  if (!dmpReady) return;
  // read a packet from FIFO
  if (mpu.dmpGetCurrentFIFOPacket(fifoBuffer)) {
#ifdef OUTPUT_READABLE_QUATERNION
    // display quaternion values in easy matrix form: w x y z
    mpu.dmpGetQuaternion(&q, fifoBuffer);
    Serial.print(q.w);
    Serial.print(",");
    Serial.print(q.x);
    Serial.print(",");
    Serial.print(q.y);
    Serial.print(",");
    Serial.println(q.z);
#endif

#ifdef OUTPUT_READABLE_YAWPITCHROLL
    mpu.dmpGetQuaternion(&q, fifoBuffer);
    mpu.dmpGetGravity(&gravity, &q);
    mpu.dmpGetYawPitchRoll(ypr, &q, &gravity);
    float roll = ypr[2] * 180 / M_PI;
    float pitch = ypr[1] * 180 / M_PI;
    float yaw = ypr[0] * 180 / M_PI;
    Serial.print("Gyroscope data| ");
    Serial.print("Roll: ");
    Serial.print(roll);  // roll
    Serial.print(", ");
    Serial.print("Pitch: ");
    Serial.print(pitch);  // pitch
    Serial.print(", ");
    Serial.print("Yaw: ");
    Serial.print(yaw);  // yaw
    Serial.print("\t\t");
#endif
  }

  // Read accelerations and angular velocities
  mpu.getAcceleration(&ax, &ay, &az);
  mpu.getRotation(&gx, &gy, &gz);


  // Use complementary and kalman filter
  updateFiltered();

  // Print roll and pitch angle with complementary and kalman filter
  Serial.print("complementary filter data| ");
  Serial.print("Roll: ");
  Serial.print(compAngleX);
  Serial.print(", ");
  Serial.print("Pitch: ");
  Serial.print(compAngleY);
  Serial.print("\t\t");
  Serial.print("Kalman filter data| ");
  Serial.print("Roll: ");
  Serial.print(kalAngleX);
  Serial.print(", ");
  Serial.print("Pitch: ");
  Serial.print(kalAngleY);
  Serial.print("\r\n");

  delay(10);
}
