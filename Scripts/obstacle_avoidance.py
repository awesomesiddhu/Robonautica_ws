#! /usr/bin/env python

import rospy
import time
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

pub = None

def clbk_laser(msg):
    """
    regions = {
        'right':  min(min(msg.ranges[0:143]), 10),
        'fright': min(min(msg.ranges[144:287]),10),
        'front':  min(min(msg.ranges[288:431]), 10),
        'fleft':  min(min(msg.ranges[432:575]), 10),
        'left':   min(min(msg.ranges[576:713]), 10),
    }
    
    regions = {
        'front':  min(min(msg.ranges[0:51]),10),
        'fleft': min(min(msg.ranges[52:103]),10),
        'left':  min(min(msg.ranges[104:155]),10),
        'fright':  min(min(msg.ranges[156:207]),10),
        'right':   min(min(msg.ranges[208:259]),10),
    }
    
    regions = {
        'front':  min(min([x for x in msg.ranges[0:51] if x>=1 and x<=3]),10),
        'fleft': min(min([x for x in msg.ranges[52:103] if x>=1 and x<=3]),10),
        'left':  min(min([x for x in msg.ranges[104:155] if x>=1 and x<=3]),10),
        'fright':  min(min([x for x in msg.ranges[156:207] if x>=1 and x<=3]),10),
        'right':   min(min([x for x in msg.ranges[208:259] if x>=1 and x<=3]),10)
    }
    """
    regions = {
        'front':  min(min([x for x in msg.ranges[110:120] if x<=6]),10),
        'fleft': min(min([x for x in msg.ranges[120:130] if x<=6]),10),
        'left':  min(min([x for x in msg.ranges[130:140] if x<=6]),10),
        'fright':  min(min([x for x in msg.ranges[140:150] if x<=6]),10),
        'right':   min(min([x for x in msg.ranges[150:160] if x<=6]),10),
    }
    
    
    take_action(regions)
    
    
def take_action(regions):
    msg = Twist()
    linear_x = 0
    angular_z = 0

    state_description = ''

    if regions['front'] > .5:
        state_description = 'case 1 - No obstacle'
        linear_x = 0.3
        angular_z = 0
    elif regions['front'] < .5 and regions['fleft'] > .5 and regions['fright'] > .5:
        state_description = 'case 2 - Forward obstacle'
        linear_x = 0.1
        if regions['front'] > .5 and regions['fleft'] > .5 and regions['fright'] < .5:
            linear_x = 0.1
            angular_z = 0.8
        else:
            linear_x = 0.1
            angular_z = -0.8
    elif regions['front'] > .5 and regions['fleft'] > .5 and regions['fright'] < .5:
        state_description = 'case 3 - Front right obstacle'
        linear_x = 0.1
        angular_z = 0.8
    elif regions['front'] > .5 and regions['fleft'] < .5 and regions['fright'] > .5:
        state_description = 'case 4 - Front left obstacle'
        linear_x = 0.0
        angular_z = -0.8
    elif regions['front'] < .5 and regions['fleft'] > .5 and regions['fright'] < .5:
        state_description = 'case 5 - Front and front right obstacle'
        linear_x = 0.1
        angular_z = 0.8
    elif regions['front'] < .5 and regions['fleft'] < .5 and regions['fright'] > .5:
        state_description = 'case 6 - Front and front left obstacle'
        linear_x = 0.1
        angular_z = -0.8

    
    elif regions['front'] > .5 and regions['fleft'] < .5 and regions['fright'] < .5:
        state_description = 'case 8 - Front left and front right obstacle'
        linear_x = 0.3
        angular_z = 0.0
    
    else:
        linear_x= 0.1
        angular_z = 0
        state_description = 'Unknown case'
        rospy.loginfo(regions)

    rospy.loginfo(state_description)
    msg.linear.x = linear_x
    msg.angular.z = angular_z
    pub.publish(msg)
    
def main():
    global pub

    rospy.init_node('reading_laser')

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    sub = rospy.Subscriber('/scan', LaserScan, clbk_laser)

    rospy.spin()

if __name__ == '__main__':
    main()
