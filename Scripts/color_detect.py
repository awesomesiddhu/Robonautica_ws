
#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import time
lower_red = np.array([0, 40, 85])
upper_red = np.array([10, 255, 255])

lower_yellow = np.array([21, 55, 53])
upper_yellow = np.array([30, 255, 255])

lower_green = np.array([60, 75, 10])
upper_green = np.array([90, 255, 255])
time1=time.time()
def work():

    class TrafficSignDetect:

        def __init__(self):
            self.cv_bridge = CvBridge()
            self.image_sub = rospy.Subscriber("/camera/color/image_raw", Image, self.image_callback)
            #self.image_sub = rospy.Subscriber("/webcam/image_raw", Image, self.image_callback)

        def image_callback(self, msg):
            try:
                c1_frame = self.cv_bridge.imgmsg_to_cv2(msg, "bgr8")
                h,w = c1_frame.shape[:2]
                cv_frame = c1_frame[200:h-400, 400:w-400]
                hsv = cv2.cvtColor(cv_frame, cv2.COLOR_BGR2HSV)

                # Create masks for each color
                mask_red = cv2.inRange(hsv, lower_red, upper_red)
                mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
                mask_green = cv2.inRange(hsv, lower_green, upper_green)

                # Find contours in the masks
                contours_red = cv2.findContours(mask_red.copy(), cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE)[-2]
                contours_yellow = cv2.findContours(mask_yellow.copy(), cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE)[-2]
                contours_green = cv2.findContours(mask_green.copy(), cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE)[-2]
                
                cv2.imshow("frame", cv_frame)
                # If a contour was found
                if len(contours_red) > 10:
                    print("Red stop sign")
                    
                if len(contours_yellow) > 10:
                    print("Yellow wait sign")
                    
                if len(contours_green) > 10:
                    print("Green go sign")
                
                else:
                    pass
                
                cv2.imshow("frame", cv_frame)
                cv2.waitKey(1)
            
            except Exception as e:
                print("Exception:", e)


    
    rospy.init_node("traffic_sign_detector")
    node = TrafficSignDetect()
    rospy.spin()

work()
