#!/usr/bin/env python  
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point
import time

#this method will make the robot move to the goal location
def move_to_goal(xGoal,yGoal):

   #define a client for to send goal requests to the move_base server through a SimpleActionClient
   ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

   #wait for the action server to come up
   while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
           rospy.loginfo("Waiting for the move_base action server to come up")

   goal = MoveBaseGoal()
   
   
   #set up the frame parameters
   goal.target_pose.header.frame_id = "map"
   goal.target_pose.header.stamp = rospy.Time.now()

   # moving towards the goal*/

   goal.target_pose.pose.position =  Point(xGoal,yGoal,0)
   goal.target_pose.pose.orientation.x = 0.0
   goal.target_pose.pose.orientation.y = 0.0
   goal.target_pose.pose.orientation.z = 0.0
   goal.target_pose.pose.orientation.w = 1.0

   rospy.loginfo("Sending goal location ...")
   ac.send_goal(goal)

   ac.wait_for_result(rospy.Duration(60))

   rospy.loginfo("Robot has reached the destination")
   return True

if __name__ == '__main__':
	start = time.time()
	rospy.init_node('map_navigation', anonymous=False)
	file1 = open('MarkerPoseLocations.txt', 'r')
	Lines = file1.readlines()
	for line in Lines:
		coord = line.strip().split()
		marker_ID = coord[0]
		x_goal = coord[1]
		y_goal = coord[2]
		if(move_to_goal(float(x_goal),float(y_goal))):
			print(x_goal, y_goal, "is the pose.",marker_ID, "is number stored in ArUco marker.")
			time.sleep(3)
	end = time.time()
	print("time taken in seconds", start-end)
	rospy.spin()
	
