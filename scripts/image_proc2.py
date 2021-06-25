#!/usr/bin/env python
import rospy
import os
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge
import cv2
import numpy as np

# webcamera enkensyutu

l = []
j = []

def process_image(msg):
    try:
        bridge = CvBridge()
        orig = bridge.imgmsg_to_cv2(msg, "bgr8")
        img = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
	
        #img = cv2.Canny(img, 15.0, 30.0)
	#img = cv2.blur(img, (7, 7))
	#cv2.circle(img, (190, 35), 15, (255, 255, 255), thickness=-1)
	#cv2.circle(img, (240, 35), 20, (0, 0, 0), thickness=3, lineType=cv2.LINE_AA)
	circles = cv2.HoughCircles (img, cv2.HOUGH_GRADIENT, 1, 20, param1 = 500, param2 = 30, minRadius = 0, maxRadius = 0)
	circles = np . uint16 ( np . around ( circles ) )

	
	
	#a = []
	for i in circles [ 0 , : ] :
	    cv2.circle ( orig, (i[0], i[1]), i[2], (0, 255, 0), 2 )
	    cv2.circle ( orig, (i[0], i[1]), 2   , (0, 0, 255), 3 )
	    #a.append(i)
	    l.append(i[0])
	    j.append(i[1])
	    #print(l)
	    
	    #print(j)
            #a = i[0] 

            #print (l[0], j[0])
            #print (l[4], j[4])
	   
            
        #print(circles [0,0])

	imgMsg = bridge.cv2_to_imgmsg(img, "mono8")
        pub = rospy.Publisher('image_gray', Image, queue_size=10)
        pub.publish(imgMsg)

	cv2.imshow('image', orig)
        cv2.waitKey(1)
 
    except Exception as err:
        print err

def start_node():
    rospy.init_node('img_proc')
    rospy.loginfo('img_proc node started')
    rospy.Subscriber("image_raw", Image, process_image)
    rospy.spin()

if __name__ == '__main__':
    try:
        start_node()
    except rospy.ROSInterruptException:
        pass
