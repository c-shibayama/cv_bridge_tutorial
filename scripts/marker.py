

import rospy
import math
from visualization_msgs.msg import Marker

rospy.init_node("marker_pub")

pub = rospy.Publisher("arrow_pub", Marker, queue_size = 10)
rate = rospy.Rate(25)

w=0

while not rospy.is_shutdown():
    marker_data = Marker()
    marker_data.header.frame_id = "base_link"
    marker_data.header.stamp = rospy.Time.now()

    marker_data.ns = "basic_shapes"
    marker_data.id = 0

    marker_data.action = Marker.ADD

    marker_data.pose.position.x = 3.0
    marker_data.pose.position.y = 0.0
    marker_data.pose.position.z = 0.0

    marker_data.pose.orientation.x=0.0
    marker_data.pose.orientation.y=0.0
    marker_data.pose.orientation.z=math.sin(math.pi/4)
    marker_data.pose.orientation.w=math.cos(math.pi/4)

    marker_data.color.r = 1.0
    marker_data.color.g = 0.0
    marker_data.color.b = 0.0
    marker_data.color.a = 1.0

    marker_data.scale.x = 1
    marker_data.scale.y = 0.1
    marker_data.scale.z = 0.1

    marker_data.lifetime = rospy.Duration()

    marker_data.type = 0

    pub.publish(marker_data)

    rate.sleep()
