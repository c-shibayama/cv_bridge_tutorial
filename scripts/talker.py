#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64MultiArray

def talker():
    pub = rospy.Publisher('chatter', Float64MultiArray, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    array = list(range(3))
    while not rospy.is_shutdown():
        a = map(float, raw_input().split())
        array[0] = a[0]
        array[1] = a[1]
        array[2] = a[2]
        array_forPublish = Float64MultiArray(data=array)
        pub.publish(array_forPublish)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
