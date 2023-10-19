import rospy
from nav_msgs.msg import Odometry
import time
import sys

def callback(data):
    print(data.pose.pose.position)
    print(data.pose.pose.orientation)
    time.sleep(1)
    sub.unregister()
    sys.exit()

rospy.init_node('pose_recorder')
sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()
