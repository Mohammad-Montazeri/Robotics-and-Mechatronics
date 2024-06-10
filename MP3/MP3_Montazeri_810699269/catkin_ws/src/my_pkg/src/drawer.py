#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn, Kill, TeleportAbsolute
from std_srvs.srv import Empty
from turtlesim.msg import Pose
from numpy import deg2rad, arange
import sys
import select
import termios
import tty

# Map arrow key escape sequences to velocities
key_mapping = {
    "\x1b[A": [1, 0],   # Up arrow - Go Forward
    "\x1b[B": [-1, 0],  # Down arrow - Go Backward
    "\x1b[C": [0, 1],   # Right arrow - Go Rightward
    "\x1b[D": [0, -1],  # Left arrow - Go Leftward
}


def get_key():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(3)
    else:
        key = ""
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    # print(key)
    return key


# Flush the input buffer
def flush_input():
    termios.tcflush(sys.stdin, termios.TCIFLUSH)


def Change_bg_color(r=250, g=250, b=50):
    rospy.set_param("/turtlesim/background_r", r)
    rospy.set_param("/turtlesim/background_g", g)
    rospy.set_param("/turtlesim/background_b", b)
    rospy.wait_for_service("/clear")
    try:
        bg_color = rospy.ServiceProxy("/clear", Empty)
        kill_turtle = rospy.ServiceProxy("/kill", Kill)
        resp1 = bg_color()
        resp2 = kill_turtle("turtle1")
        return resp1, resp2
    except rospy.ServiceException as e:
        rospy.loginfo(f"Error in Change_bg_color with the exception {e}")


def Drawer(control_type):
    rospy.wait_for_service("/spawn")
    try:
        turtles_list = []
        spawn_client = rospy.ServiceProxy("/spawn", Spawn)
        delay = 0.05
        if control_type == 1:
            t_list = Turtle_pixel_one(turtles_list, spawn_client, delay)
        elif control_type == 2:
            t_list = Turtle_pixel_two(turtles_list, spawn_client, delay)
        else:
            print("Unsupported character number!")
            return False

        print(f"number of turtles = {len(t_list)}")
        print(f"list of turtles: {t_list}")
        return t_list

    except rospy.ServiceException as e:
        print(f"Error in Drawer with the exception {e}")


def Turtle_pixel_one(turtles_list, spawn_client, delay):
    i, j, k = 1, 1, 1
    for col in range(1, 11):
        x, y, th, name = col, 10, 0, f"t{i}"
        if col == 1:
            y = 9.6
            th = deg2rad(30)
        elif col == 10:
            y = 10.4
            th = deg2rad(30)
        spawn_client(x, y, th, name)
        turtles_list.append(name)
        rospy.sleep(delay)
        i += 1

    for row in range(9, 1, -1):
        name = f"t{i}"
        y = row
        if row >= 8:
            x1, x2 = 1.50, 10
            th = deg2rad(90)
            name1, name2 = name + "_1", name + "_2"
            spawn_client(x1, y, -th, name1)
            spawn_client(x2, y, th, name2)
            turtles_list.extend([name1, name2])
        elif 6 <= row <= 7:
            x1, x2, x3 = 1.45 + j / 4, 10 - j / 4, 5.75
            th = deg2rad(90 - 10 * j)
            name1, name2, name3 = name + "_1", name + "_2", name + "_3"
            spawn_client(x1, y, -th, name1)
            spawn_client(x2, y, th, name2)
            spawn_client(x3, y, 0, name3)
            turtles_list.extend([name1, name2, name3])
            j += 1
        elif 3 <= row <= 5:
            x1, x2, x3, x4 = 1.45 + j / 3, 10 - j / 3, 5.75 - k / 3, 5.75 + k / 3
            th = deg2rad(90 - 12 * j)
            name1, name2, name3, name4 = (
                name + "_1",
                name + "_2",
                name + "_3",
                name + "_4",
            )
            spawn_client(x1, y, -th, name1)
            spawn_client(x2, y, th, name2)
            spawn_client(x3, y, th, name3)
            spawn_client(x4, y, -th, name4)
            turtles_list.extend([name1, name2, name3, name4])
            j += 1
            k += 1
        elif row == 2:
            x1, x2, x3, x4 = 1.45 + j / 2, 10 - j / 2, 5.75 - k / 2, 5.75 + k / 2
            th = deg2rad(90 - 15 * j)
            y = y + 0.3
            name1, name2, name3, name4 = (
                name + "_1",
                name + "_2",
                name + "_3",
                name + "_4",
            )
            spawn_client(x1, y, -th, name1)
            spawn_client(x2, y, th, name2)
            spawn_client(x3, y, th, name3)
            spawn_client(x4, y, -th, name4)
            turtles_list.extend([name1, name2, name3, name4])
        i += 1
        rospy.sleep(delay)

    return turtles_list


def Turtle_pixel_two(turtles_list, spawn_client, delay):
    th = 0
    i, k, s = 1, 2, 2
    for col in arange(8, 1.9, -0.6):
        x, y, name = col, 10, f"t{i}"
        spawn_client(x, y, th, name)
        turtles_list.append(name)
        rospy.sleep(delay)
        i += 1

    for row in arange(9.6, 0, -0.4):
        y, name = row, f"t{i}"
        if row > 8.2:
            x = 2
        elif row == 8.2:
            x = 2.4
        elif 4.4 <= row < 8.2:
            x = x + s / k**1.6 + 1.2 / k
            k += 1.6
            s += 1.7
        elif 3.8 < row < 4.4:
            pass  # belly point of number '5'
        elif row < 3.8:
            k -= 1.6
            s -= 1.7
            x = x - s / k**1.6 - 1.2 / k

        spawn_client(x, y, th, name)
        turtles_list.append(name)
        rospy.sleep(delay)

        i += 1

    return turtles_list


def Move_turtles(speed, angular_z, turtles_list):
    # Wait for the clear service to become available
    rospy.wait_for_service("/clear")

    # Call the clear service to clear the background
    try:
        clear_service = rospy.ServiceProxy("/clear", Empty)
        clear_service()
    except rospy.ServiceException as e:
        print(f"Error in Move_turtles with the exception {e}")

    # Publish the velocity message to each turtle
    publishers = []
    monitor = [0 for i in range(len(turtles_list))]

    rate = rospy.Rate(5)  # 5 Hz
    counter = 0

    for i, turtle_name in enumerate(turtles_list):
        monitor[i] = Turtle_pose(turtle_name)

    while not rospy.is_shutdown():
        flush_input()  # Flush input buffer to avoid delays
        key = get_key()
        velocity_msg = Twist()
        if key in key_mapping:

            for obj in monitor:
                pose = obj.get_theta()
                if pose is None:
                    continue
                obj.set_orientation()

            velocities = key_mapping[key]

            # Define the velocity message
            velocity_msg.linear.x = velocities[1] * speed
            velocity_msg.linear.y = velocities[0] * speed

        else:
            velocity_msg.angular.z = angular_z

        # Retrieve the list of turtle topics
        for trtl in turtles_list:
            topic = f"/{trtl}/cmd_vel"
            publisher = rospy.Publisher(topic, Twist, queue_size=1)
            publishers.append(publisher)

        for publisher in publishers:
            publisher.publish(velocity_msg)
        print(f"motion - {counter}")
        counter += 1
        rate.sleep()


# Define the class to set the turtle's orientation to zero
class Turtle_pose:
    def __init__(self, trtl) -> None:
        self.turtle = trtl
        self.pose = None
        self.subscriber = rospy.Subscriber(
            f"/{trtl}/pose", Pose, self.callback)

    def callback(self, pose):
        """
        Callback function to handle pose messages.
        Updates the theta value with the current turtle orientation.
        """
        # current_theta = pose.theta
        # print(f"current angle of turtle {self.turtle} is {current_theta}")
        self.pose = [pose.x, pose.y, pose.theta]

    def get_theta(self):
        """
        Returns the current theta value.
        If theta is None, indicates no pose data has been received yet.
        """
        if self.pose is not None:
            return self.pose
        else:
            print(f"No pose data received for {self.turtle} yet.")
            return None

    def set_orientation(self):
        rospy.wait_for_service(f"/{self.turtle}/teleport_absolute")
        velocity_msg = Twist()
        try:
            teleport_service = rospy.ServiceProxy(
                f"/{self.turtle}/teleport_absolute", TeleportAbsolute
            )

            if self.pose is not None:
                # Setting theta to 0 radians (facing right)
                teleport_service(self.pose[0], self.pose[1], 0)

                # Setting theta_dot to 0 radians/s (zero angular velocity)
                velocity_msg.angular.z = 0
                topic = f"/{self.turtle}/cmd_vel"
                publisher = rospy.Publisher(topic, Twist, queue_size=1)
                publisher.publish(velocity_msg)

        except rospy.ServiceException as e:
            print(f"Error in Set_orientation: {e}")


if __name__ == "__main__":
    settings = termios.tcgetattr(sys.stdin)
    try:
        # initial node
        rospy.init_node("TurtleCharacter")
        print("App initialized")
        control_type = rospy.get_param("~character", 1)
        respond1 = Change_bg_color()
        respond2 = Drawer(control_type)
        rospy.sleep(1.2)  # sleep 1.2 seconds before rotating turtles
        print(" Starting rotation... \n Use arrow keys to move the turtles.")
        respond3 = Move_turtles(
            speed=1, angular_z=deg2rad(30), turtles_list=respond2)
        print(respond1, respond2, respond3, sep="\t|\t")

    except:
        print("An error occurred at the beginning")

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
