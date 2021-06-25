#!/usr/bin/env python
import os
import rospy
import cv2
from std_msgs.msg import Float64MultiArray
import numpy as np


# gazou yomikomi enkensyutu


def operator():
    #rospy.init_node('operator', anonymous=True)
    #pub = rospy.Publisher('image_data', Image, queue_size=10)

    # read image
    #filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lena.png')
    #im = cv2.imread(filepath, cv2.IMREAD_COLOR)
    #cv2.imshow('image', im)
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

 





    # make bridge
    #bridge = CvBridge()
    #msg = bridge.cv2_to_imgmsg(im, encoding="bgr8")
    #rate = rospy.Rate(1) # 1hz
    #while not rospy.is_shutdown():
        #pub.publish(msg)
        #rate.sleep()

if __name__ == '__main__':
    try:
        operator()
    except rospy.ROSInterruptException:
        pass

