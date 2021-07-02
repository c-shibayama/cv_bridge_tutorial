#!/usr/bin/env python
import os
import rospy
import cv2
from std_msgs.msg import Float64MultiArray
import numpy as np


# gazou yomikomi enkensyutu
# and 
# position wo test52 he publish


def operator():

    img = cv2.imread('src/cv_bridge_tutorial/scripts/ball.jpg')

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles (img, cv2.HOUGH_GRADIENT, 1, 40, param1 = 500, param2 = 15, minRadius = 0, maxRadius = 0)
    circles = np . uint16 ( np . around ( circles ) )
    if circles is not None:
        for i in circles [ 0 , : ] :
	    cv2.circle ( img, (i[0], i[1]), i[2], (0, 255, 0), 2 )
	    cv2.circle ( img, (i[0], i[1]), 2   , (0, 0, 255), 3 )
	    print (i[0], i[1])
            

    pub = rospy.Publisher('circle', Float64MultiArray, queue_size=10)
    rospy.init_node('gazou', anonymous=True)
    r = rospy.Rate(10)


    array = list(range(3))
    array[0] = i[0]*0.01*0.1
    array[1] = i[1]*0.01*0.1
    array[2] = 0.3
    posi = Float64MultiArray(data=array)
    pub.publish(posi)

    path = os.getcwd()
    print(path)

    cv2.imshow('image', img)
    cv2.waitKey(0)



if __name__ == '__main__':
    try:
        operator()
    except rospy.ROSInterruptException:
        pass

