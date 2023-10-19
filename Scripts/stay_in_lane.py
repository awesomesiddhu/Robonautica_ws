#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
from cv_bridge import CvBridge
import cv2
import numpy as np
max_slider = 10
linear_x = 0.2
angular_z = 0.0
state = 0
def work():

    vel_msg = Twist()
    global linear_x
    global angular_z
    global state


    class Lane_Follower:

        def __init__(self):
            self.cv_bridge = CvBridge()
            
            self.image_sub = rospy.Subscriber("/camera/color/image_raw", Image, self.image_callback)
            #self.image_sub = rospy.Subscriber("/webcam/image_raw", Image, self.image_callback)


        def image_callback(self, msg):
            state = 0
            try:
                c1_frame = self.cv_bridge.imgmsg_to_cv2(msg, "bgr8")
                h,w = c1_frame.shape[:2]
                cv_frame = c1_frame[450:h-50, 400:w-400]
                frame = cv2.GaussianBlur(cv_frame, (5, 5), 0)

                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                low_yellow = np.array([12, 50, 90])
                up_yellow = np.array([32, 255, 255])

                mask = cv2.inRange(hsv, low_yellow, up_yellow)
                edges = cv2.Canny(mask, 75, 150)
                lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=50)

                # Initialize variables to keep track of detected lanes
                left_lane_found = False
                right_lane_found = False

                # Loop through the detected lines
                if lines is not None:
                    for line in lines:
                        x1, y1, x2, y2 = line[0]
                        # Calculate the slope of the line
                        slope = (y2 - y1) / (x2 - x1)

                        # Determine which lane the line belongs to
                        if slope > 0:
                            left_lane_found = True
                        else:
                            # It's a right lane
                            right_lane_found = True

                # Make decisions based on the detected lanes
                if left_lane_found and right_lane_found:
                    print('forward')
                    global linear_x
                    global angular_z
                    linear_x=0.3
                elif left_lane_found:
                    print('go right')
                    state = 1
                    linear_x = 0.07
                    angular_z = 0.2
                elif right_lane_found:
                    print('go left')
                    state = 0
                    linear_x = 0.07
                    angular_z = -0.2
                else:
                    if state==1:
                        linear_x = 0.02
                        angular_z = 0.2
                    else:
                        linear_x = 0.02
                        angular_z = -0.2
                        
                

                cv2.imshow("Lane Following Robot", edges)
                cv2.imshow("frame", frame)
                cv2.waitKey(1)
                
            
            except Exception as e:
                print("Exception:", e)

            vel_msg.linear.x = linear_x
            vel_msg.angular.z = angular_z
            
            pub.publish(vel_msg)

    rospy.init_node("lane_detect")
    node = Lane_Follower()
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    
    rospy.spin()

work()
