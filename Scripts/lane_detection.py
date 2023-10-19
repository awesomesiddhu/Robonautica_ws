#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

def work():

    class LaneFollower:

        def __init__(self):
            self.cv_bridge = CvBridge()
            self.image_sub = rospy.Subscriber("/camera/color/image_raw", Image, self.image_callback)

        def image_callback(self, msg):
            try:
                cv_frame = self.cv_bridge.imgmsg_to_cv2(msg, "bgr8")
                
                frame = cv2.GaussianBlur(cv_frame, (5, 5), 0)
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

                low_yellow = np.array([30,94,140])
                up_yellow = np.array([30, 255, 255])

                mask = cv2.inRange(hsv, low_yellow, up_yellow)
                edges = cv2.Canny(mask, 75, 150)
                lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)
                print(lines)


                if lines is not None:

                    # Find the center of the lane
                    lane_center = (lines[0][0][0] + lines[0][0][2]) // 2, (lines[0][0][1] + lines[0][0][3]) // 2

                    # Calculate the distance from the center of the lane to the center of the car
                    car_center = (frame.shape[1] // 2, frame.shape[0] // 2)
                    distance_to_lane_center = np.linalg.norm(np.array(lane_center) - np.array(car_center))

                    # Calculate the offset from the lane
                    offset_from_lane = distance_to_lane_center - frame.shape[1] #viewport width.

                    print(f"Offset from lane: {offset_from_lane} pixels")

                    for line in lines:
                        x1, y1, x2, y2 = line[0]
                        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

                    # Display the frame and offset
                    cv2.imshow("frame", frame)
                    cv2.imshow("edges", edges)

                    cv2.waitKey(25)
                    
            except Exception as e:
                #print("Exception:", e)
                pass

    rospy.init_node("lane_follower")
    node = LaneFollower()
    rospy.spin()

work()
