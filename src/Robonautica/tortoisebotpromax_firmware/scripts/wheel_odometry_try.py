#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO
import time
from std_msgs.msg import Int16

leftEn = 12			#	Purple
rightEn = 13		#	Red

leftBackward = 5	#	Blue
leftForward = 6		#	Green
rightForward = 16	#	Yellow
rightBackward = 20	#	Orange

publ = None
pubr = None

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(leftEn, GPIO.OUT)
GPIO.setup(rightEn, GPIO.OUT)



def elkflse():
    while(1):
        leftEnval = GPIO.read(leftEn)
        rightEnval = GPIO.read(rightEn)
        publ.publish(leftEnval)
        pubr.publish(rightEnval)

def main():
    rospy.init_node('wheel_odometry', anonymous=False)
    pubr = rospy.Publisher("/rwheel", Int16)
    publ = rospy.Publisher("/lwheel", Int16)
    rospy.spin()   

if __name__== '__main__':
    main()
