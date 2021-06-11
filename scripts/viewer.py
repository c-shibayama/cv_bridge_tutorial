#!/usr/bin/env python
import rospy
import cv2

from cv_bridge import CvBridge
from sensor_msgs.msg import Image

def process_image(msg):
    try:
        bridge = CvBridge()
        img = bridge.imgmsg_to_cv2(msg, "mono8")
	#img = cv2.Canny(orig, 15.0, 30.0)
	cv2.circle(img, (190, 35), 15, (255, 255, 255), thickness=-1)
	cv2.circle(img, (240, 35), 20, (0, 0, 0), thickness=3, lineType=cv2.LINE_AA)

        cv2.imshow('img', img)
        cv2.waitKey(10)
    except Exception as err:
        print err

def start_node():
    rospy.init_node('viewer')
    rospy.loginfo('viewer node started')
    rospy.Subscriber("image_gray", Image, process_image)
    rospy.spin()

if __name__ == '__main__':
    try:
        start_node()
    except rospy.ROSInterruptException:
        pass
