#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray

def callback(data):
    rospy.loginfo('%f, %f', data.data[0], data.data[1])
    print(data.data)
def listener():

    # in ROS, nodes are unique named. If two nodes with the same
    # node are launched, the previous one is kicked off. The 
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaenously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", Float64MultiArray, callback)

    #print()

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
        
if __name__ == '__main__':
    listener()
