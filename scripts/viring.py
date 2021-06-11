#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge
import cv2

def process_image(msg):
    try:
        face_cascade_path = '/home/cshiba/opencv/data/haarcascade_frontalface_default.xml'
	eye_cascade_path = '/home/cshiba/opencv/data/haarcascades/haarcascade_eye.xml'

	face_cascade = cv2.CascadeClassifier(face_cascade_path)
	eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

	cap = cv2.VideoCapture(0)

	while True:
	    bridge = CvBridge()
            img = bridge.imgmsg_to_cv2(msg, "bgr8")
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

	    for x, y, w, h in faces:
    	        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    	        face = src[y: y + h, x: x + w]
                face_gray = src_gray[y: y + h, x: x + w]
   	        eyes = eye_cascade.detectMultiScale(face_gray)
    	        for (ex, ey, ew, eh) in eyes:
               	    cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

	    cv2.imshow('video image', img)
	    cv2.waitKey(1)
            key = cv2.waitKey(10)
            if key == 27:  
                break

        cap.release()
        cv2.destroyAllWindows()
	
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
