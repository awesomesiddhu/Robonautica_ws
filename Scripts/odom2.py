#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from nav_msgs.msg import Odometry

class OdometryCalculator:
    def __init__(self):
        self.left_vel = 0.0
        self.right_vel = 0.0
        self.last_time = rospy.Time.now()

        self.odom_pub = rospy.Publisher('odom', Odometry, queue_size=10)
        rospy.Subscriber('left_vel', Float32, self.left_vel_callback)
        rospy.Subscriber('right_vel', Float32, self.right_vel_callback)

    def left_vel_callback(self, msg):
        self.left_vel = msg.data

    def right_vel_callback(self, msg):
        self.right_vel = msg.data

    def calculate_odometry(self):
        current_time = rospy.Time.now()
        dt = (current_time - self.last_time).to_sec()
        self.last_time = current_time

        # Assuming acceleration is the change in velocity over time
        left_acceleration = self.left_vel / dt
        right_acceleration = self.right_vel / dt

        # Calculate displacement using s=ut+0.5*a*t^2
        left_displacement = self.left_vel * dt + 0.5 * left_acceleration * dt * dt
        right_displacement = self.right_vel * dt + 0.5 * right_acceleration * dt * dt

        # Assuming the robot moves by the average of the left and right displacements
        displacement = (left_displacement + right_displacement) / 2

        # Create and publish odometry message
        odom_msg = Odometry()
        odom_msg.header.stamp = current_time
        odom_msg.pose.pose.position.x += displacement  # Update this to include orientation if your robot can move in more than one direction
        self.odom_pub.publish(odom_msg)

if __name__ == '__main__':
    rospy.init_node('odometry_calculator')
    oc = OdometryCalculator()
    rate = rospy.Rate(10)  # 10 Hz
    while not rospy.is_shutdown():
        oc.calculate_odometry()
        rate.sleep()
