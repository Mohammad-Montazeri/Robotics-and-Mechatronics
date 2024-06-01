#include "I2Cdev.h"
#include <Kalman.h>
#include "Wire.h"
#include "MPU6050_6Axis_MotionApps20.h"

// Variables related to complementary filter data
int ax, ay, az;
int gx, gy, gz;

long tiempo_prev;
float dt;

// Variables related to kalman filter data
// Create the Kalman instances
Kalman kalmanX;
Kalman kalmanY;

// for calculate time
int16_t tempRaw;

double kalAngleX, kalAngleY;  // Calculated angle using a Kalman filter


const int mpuAddress = 0x68;  // It can be 0x68 or 0x69
MPU6050 mpu(mpuAddress);


void updateFiltered() {
  // Calculate the execution time of the function in each round
  dt = (micros() - tiempo_prev) / 1000000.0;
  tiempo_prev = micros();

  //Calculate the angles with accelerometer
  float roll = atan2(ay, az) * (180.0 / M_PI);
  float pitch = atan2(-ax, az) * (180.0 / M_PI);

  double gyroXrate = gx / 131.0;  // Convert to deg/s
  double gyroYrate = gy / 131.0;  // Convert to deg/s
  double gyroZrate = gz / 131.0;  // Convert to deg/s

  if ((roll < -90 && kalAngleX > 90) || (roll > 90 && kalAngleX < -90)) {
    kalmanX.setAngle(roll);
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
    kalAngleY = pitch;
  } else {
    kalAngleY = kalmanY.getAngle(pitch, gyroYrate, dt);  // Calculate the angle using a Kalman filter
  }

  if (abs(kalAngleY) > 90) {
    gyroXrate = -gyroXrate;  // Invert rate, so it fits the restriced accelerometer reading
  }
  kalAngleX = kalmanX.getAngle(roll, gyroXrate, dt);  // Calculate the angle using a Kalman filter
}


void setup() {
  delay(1000);  // Wait for sensor to stabilize
  Serial.begin(115200);
  Wire.begin();
  // complementary and kalman filter
  mpu.initialize();
  // calculate roll and pitch angle as primary data
  float roll = atan2(mpu.getAccelerationY(), mpu.getAccelerationZ()) * (180.0 / M_PI);
  float pitch = atan2(-mpu.getAccelerationX(), mpu.getAccelerationZ()) * (180.0 / M_PI);
  // Set starting angle
  kalmanX.setAngle(roll);
  kalmanY.setAngle(pitch);
}

void loop() {
  // Read accelerations and angular velocities
  mpu.getAcceleration(&ax, &ay, &az);
  mpu.getRotation(&gx, &gy, &gz);


  // Use complementary and kalman filter
  updateFiltered();

  // Print roll and pitch angle with kalman filter
  Serial.print(kalAngleX);
  Serial.print(",");
  Serial.print(kalAngleY);
  Serial.print("\r\n");

  delay(10);
}
