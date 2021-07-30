#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge
import cv2
import numpy as np
from std_msgs.msg import Float64MultiArray
import math

# webcamera opencv de byouga wo publish

def process_image(msg):
    try:
        bridge = CvBridge()
        orig = bridge.imgmsg_to_cv2(msg, "bgr8")
        img = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
	
        #img = cv2.Canny(img, 15.0, 30.0)
	#img = cv2.blur(img, (7, 7))
	#cv2.circle(img, (190, 35), 15, (255, 255, 255), thickness=-1)
	#cv2.circle(img, (240, 35), 20, (0, 0, 0), thickness=3, lineType=cv2.LINE_AA)
	#circles = cv2.HoughCircles (img, cv2.HOUGH_GRADIENT, 1, 20, param1 = 500, param2 = 30, minRadius = 0, maxRadius = 0)
	#circles = np . uint16 ( np . around ( circles ) )
	#for i in circles [ 0 , : ] :
	    #cv2 . circle ( img , ( i [ 0 ] , i [ 1 ] ) , i [ 2 ] , ( 0 , 255 , 0 ) , 2 )
	    #cv2 . circle ( img , ( i [ 0 ] , i [ 1 ] ) , 2 , ( 0 , 0 , 255 ) , 3 )
	    #print (i[0], i[1])

	imgMsg = bridge.cv2_to_imgmsg(img, "mono8")
        pub = rospy.Publisher('image_gray', Image, queue_size=10)
        pub.publish(imgMsg)

	cv2.imshow('image', img)
        cv2.setMouseCallback('image', onMouse)
        
        #print(img.shape)
        cv2.waitKey(1)
    except Exception as err:
        print err

def onMouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        x = x - 640/2
        y = y - 480/2
        print(x, y)
        pub = rospy.Publisher('click', Float64MultiArray, queue_size=10)
        array = list(range(3))
        array[0] = x*0.01
        array[1] = y*0.01
        array[2] = -3
        posi = Float64MultiArray(data=array)
        pub.publish(posi)

        ztheta = math.pi/2
        ytheta = 0
        xtheta = -math.pi/2
        Rz = np.array([[math.cos(ztheta), -math.sin(ztheta), 0], [math.sin(ztheta), math.cos(ztheta), 0], [0, 0, 1]])
        #print(Rz)
        Ry = np.array([[math.cos(ytheta), 0, math.sin(ytheta)], [0, 1, 0], [-math.sin(ytheta), 0, math.cos(ytheta)]])
        Rx = np.array([[1, 0, 0], [0, math.cos(xtheta), -math.sin(xtheta)], [0, math.sin(xtheta), math.cos(xtheta)]])
        R = np.dot(np.dot(Rz, Ry), Rx)
        print(R)
        
        rearray = np.dot(R, np.array([[0],[0],[3]])) + np.array([[3],[0],[0]])
        print(rearray)














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
