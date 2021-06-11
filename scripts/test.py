#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge
import cv2

def process_image(msg):
    try:
        bridge = CvBridge()
        orig = bridge.imgmsg_to_cv2(msg, "bgr8")
        #img = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
        #img = cv2.Canny(img, 15.0, 30.0)
	#img = cv2.blur(img, (7, 7))
	#cv2.circle(img, (190, 35), 15, (255, 255, 255), thickness=-1)
	#cv2.circle(img, (240, 35), 20, (0, 0, 0), thickness=3, lineType=cv2.LINE_AA)
	#cv2.imshow('image', img)
        #cv2.waitKey(1)


        frame = cv2.blur(orig, (5, 5))    
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, Numpy.array((0., self.smin, self.vmin)), np.array((180., 255., self.vmax)))
        if self.selection is not None:
	    x0, y0, w, h = self.selection
            x1 = x0 + w
            y1 = y0 + h
            self.track_window = (x0, y0, x1, y1)
            hsv_roi = hsv[y0:y1, x0:x1]
            mask_roi = mask[y0:y1, x0:x1]
            self.hist = cv2.calcHist( [hsv_roi], [0], mask_roi, [16], [0, 180] )
            cv2.normalize(self.hist, self.hist, 0, 255, cv2.NORM_MINMAX);
            self.hist = self.hist.reshape(-1)
            self.show_hist()
    
        if self.detect_box is not None:
            self.selection = None

        if self.hist is not None:
            backproject = cv2.calcBackProject([hsv], [0], self.hist, [0, 180], 1)

            backproject &= mask

            ret, backproject = cv2.threshold(backproject, self.threshold, 255, cv.CV_THRESH_TOZERO)
    
            x, y, w, h = self.track_window
            if self.track_window is None or w <= 0 or h <=0:
                self.track_window = 0, 0, self.frame_width - 1, self.frame_height - 1
                
            term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
                
            self.track_box, self.track_window = cv2.CamShift(backproject, self.track_window, term_crit)
                
                
            if len(self.track_box) == 3:
                center = self.track_box[0]
                llen = 30;
                pt1 = (int(center[0] - llen), int(center[1]))
                pt2 = (int(center[0] + llen), int(center[1]))
                pt3 = (int(center[0]), int(center[1] - llen))
                pt4 = (int(center[0]), int(center[1] + llen))
                cv2.line(self.marker_image, pt1, pt2, (255, 255, 0), 5)
                cv2.line(self.marker_image, pt3, pt4, (255, 255, 0), 5)
                
                # Display the resulting backprojection
            cv2.imshow("Backproject", backproject)
	



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
