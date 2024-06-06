#!/usr/bin/python3

import rospy
from turtlesim.srv import Spawn
from std_srvs.srv import Empty
from numpy import deg2rad

def Change_bg_color(r=250,g=250,b=50):
    rospy.set_param('/main/background_r' , r)
    rospy.set_param('/main/background_g' , g)
    rospy.set_param('/main/background_b' , b)
    rospy.wait_for_service('/clear')
    try: 
        bg_color = rospy.ServiceProxy('/clear', Empty)
        resp = bg_color()
        return resp
    except rospy.ServiceException as e:
        rospy.loginfo(f'Error in Change_bg_color with the exception {e}')

def Drawer(x, y, th, name):
    rospy.wait_for_service("/spawn")
    # rospy.init_node("Drawer")
    try:
        spawn_client = rospy.ServiceProxy('/spawn', Spawn)
        i, j, k = 1, 1, 1
        for col in range(1, 11):
            x, y, th, name = col, 10, 0, f't{i}'
            if col == 1:
                y = 9.6
                th = deg2rad(30)
            elif col == 10:
                y = 10.4
                th = deg2rad(30)
            spawn_client(x, y, th, name)
            rospy.sleep(0.2)
            i += 1
        
        for row in range(9, 1, -1):
            name = f't{i}'
            y = row
            if row >= 8:
                x1, x2 = 1.50, 10
                th = deg2rad(90)
                spawn_client(x1, y, -th, name+'_1')
                spawn_client(x2, y, th, name+'_2')
            elif 6 <= row <= 7:
                x1, x2, x3 = 1.45+j/4, 10-j/4, 5.75
                th = deg2rad(90-10*j)
                spawn_client(x1, y, -th, name+'_1')
                spawn_client(x2, y, th, name+'_2')
                spawn_client(x3, y, 0, name+'_3')
                j += 1
            elif 3 <= row <= 5:
                x1, x2, x3, x4 = 1.45+j/3, 10-j/3, 5.75-k/3, 5.75+k/3
                th = deg2rad(90-12*j)
                spawn_client(x1, y, -th, name+'_1')
                spawn_client(x2, y, th, name+'_2')
                spawn_client(x3, y, th, name+'_3')
                spawn_client(x4, y, -th, name+'_4')
                j += 1
                k += 1
            elif row == 2:
                x1, x2, x3, x4 = 1.45+j/2, 10-j/2, 5.75-k/2, 5.75+k/2
                th = deg2rad(90-15*j)
                y = y+0.3
                spawn_client(x1, y, -th, name+'_1')
                spawn_client(x2, y, th, name+'_2')
                spawn_client(x3, y, th, name+'_3')
                spawn_client(x4, y, -th, name+'_4')
            i += 1
            rospy.sleep(0.2)

    except rospy.ServiceException as e:
        print(f"Error in Drawer with the exception {e}")


if __name__ == "__main__":
    try:
        #initial node
        rospy.init_node('TurtleCharacter')
        print("App initialized")
        respond1 = Change_bg_color()
        respond2 = Drawer(4, 7, deg2rad(30), 'test')
        print(respond1, respond2)
        
    except:
        print("An error occured at the beginning")
