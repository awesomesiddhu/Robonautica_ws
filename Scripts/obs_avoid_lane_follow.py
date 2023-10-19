#! /usr/bin/env python

import rospy
import time
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

pub = None
priority_obstacle=0

def clbk_obs_laser(msg):
    regions = {
        'right':  min(min(msg.ranges[0:51]),10),
        'fright': min(min(msg.ranges[52:103]),10),
        'front':  min(min(msg.ranges[104:155]),10),
        'fleft':  min(min(msg.ranges[156:207]),10),
        'left':   min(min(msg.ranges[208:259]),10),
    }

    take_action(regions)

def clbk_lane_cam(data):
    vel_msg = Twist()
    # data.data is the offset (lane center - origin(center of frame))
    vel_msg.angular.z = -0.1*data.data
    vel_msg.linear.x = 0.5 
    if priority_obstacle==0:
        pub.publish(vel_msg)
    
    
def take_action(regions):
    msg = Twist()
    linear_x = 0
    angular_z = 0

    state_description = ''

    if regions['front'] > 1:
        state_description = 'case 1 - nothing'
        priority_obstacle=0

    else:
        if regions['front'] < 1 and regions['fleft'] > 1 and regions['fright'] > 1:
            state_description = 'case 2 - front'
            linear_x = 0.1
            if regions['front'] > 1 and regions['fleft'] > 1 and regions['fright'] < 1:
                linear_x = 0.1
                angular_z = 0.8
            else:
                linear_x = 0.1
                angular_z = -0.8
        elif regions['front'] > 1 and regions['fleft'] > 1 and regions['fright'] < 1:
            state_description = 'case 3 - fright'
            linear_x = 0.1
            angular_z = 0.8
        elif regions['front'] > 1 and regions['fleft'] < 1 and regions['fright'] > 1:
            state_description = 'case 4 - fleft'
            linear_x = 0.1
            angular_z = -0.8
        elif regions['front'] < 1 and regions['fleft'] > 1 and regions['fright'] < 1:
            state_description = 'case 5 - front and fright'
            linear_x = 0.1
            angular_z = 0.8
        elif regions['front'] < 1 and regions['fleft'] < 1 and regions['fright'] > 1:
            state_description = 'case 6 - front and fleft'
            linear_x = 0.1
            angular_z = -0.8
        elif regions['front'] < 1 and regions['fleft'] < 1 and regions['fright'] < 1:
            state_description = 'case 7 - front and fleft and fright'
            linear_x = 0.1
            angular_z = -0.8
        elif regions['front'] > 1 and regions['fleft'] < 1 and regions['fright'] < 1:
            state_description = 'case 8 - fleft and fright'
            linear_x = 0.5
            angular_z = 0.0
        else:
            state_description = 'unknown case'
            rospy.loginfo(regions)

        priority_obstacle=1   
    

    rospy.loginfo(state_description)
    msg.linear.x = linear_x
    msg.angular.z = angular_z
    if priority_obstacle==1:
        pub.publish(msg)
    
def main():
    global pub

    rospy.init_node('task2_velControl')

    rospy.Subscriber('/scan', LaserScan, clbk_obs_laser)

    rospy.Subscriber('/lane_detect', Float32, clbk_lane_cam)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    main()





