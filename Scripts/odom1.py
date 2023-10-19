
#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Quaternion, Twist
from std_msgs.msg import Float32
from tf.broadcaster import TransformBroadcaster
import tf
import math

class DiffDriveOdometry:
    def __init__(self):
        rospy.init_node('diff_drive_odometry')
        self.odom_pub = rospy.Publisher('odom', Odometry, queue_size=50)
        self.odom_broadcaster = TransformBroadcaster()

        # Robot parameters (Modify with actual values)
        self.wheel_separation = 0.242 # Distance between left and right wheels
        self.wheel_radius = 0.083/2 # Radius of the wheels

        # Current state
        self.x = 0.0 # x position
        self.y = 0.0 # y position
        self.th = 0.0 # orientation

        # Last velocities
        self.left_vel = 0.0
        self.right_vel = 0.0

        # Subscribers for wheel velocities
        rospy.Subscriber('left_vel', Float32, self.update_left_vel)
        rospy.Subscriber('right_vel', Float32, self.update_right_vel)

    def update_left_vel(self, msg):
        self.left_vel = msg.data

    def update_right_vel(self, msg):
        self.right_vel = msg.data

    def update(self, dt):
        # Compute odometry
        delta_th = (self.right_vel - self.left_vel) / self.wheel_separation * dt
        delta_x = (self.right_vel + self.left_vel) / 2 * dt * math.cos(self.th)
        delta_y = (self.right_vel + self.left_vel) / 2 * dt * math.sin(self.th)

        # Update state
        self.x += delta_x
        self.y += delta_y
        self.th += delta_th

    def publish_odom(self, current_time):
        # Create quaternion from yaw
        odom_quat = tf.transformations.quaternion_from_euler(0, 0, self.th)

        # Publish transform over tf
        self.odom_broadcaster.sendTransform(
            (self.x, self.y, 0.), odom_quat, current_time,
            "base_link", "odom"
        )

        # Create and publish odometry message
        odom = Odometry()
        
        odom.header.stamp = current_time
        
        odom.header.frame_id = "odom"
        
        odom.pose.pose.position.x = self.x
        
        odom.pose.pose.position.y = self.y
        
        odom.pose.pose.position.z = 0.
        
        odom.pose.pose.orientation.x = odom_quat[0]
        
        odom.pose.pose.orientation.y = odom_quat[1]
        
        odom.pose.pose.orientation.z = odom_quat[2]
        
        odom.child_frame_id = "base_link"
        
        vth = (self.right_vel - self.left_vel) / self.wheel_separation
        
        vx = (self.right_vel + self.left_vel) / 2.
        
        odom.twist.twist.linear.x = vx
        
        odom.twist.twist.angular.z = vth
        
        self.odom_pub.publish(odom)

if __name__ == '__main__':
    try:
      diff_drive_odom = DiffDriveOdometry()
      r = rospy.Rate(10.0)
      last_time = rospy.Time.now()
      while not rospy.is_shutdown():
          current_time = rospy.Time.now()
          dt = (current_time - last_time).to_sec()
          diff_drive_odom.update(dt)
          diff_drive_odom.publish_odom(current_time)
          last_time = current_time
          r.sleep()
    except rospy.ROSInterruptException:
      pass


