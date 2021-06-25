#!/usr/bin/env python
from core_tool import *
import rospy
import time
from threading import (Event, Thread)
from std_msgs.msg import Float64MultiArray


# enzahyou wo subscribe

positon = []

def callback(data):
    rospy.loginfo('%f, %f', data.data[0], data.data[1])
    #data.data[2] = 0.1
    global posison
    posison = data.data

def Run(ct,*args):
  ct.robot.MoveToQ([-0.02225494707637879, 0.027604753814144237, 0.02256845844164128, -2.2001560115435073, -0.00047772651727832574, 0.6569580325147487, 0.0010119170182285682], 2.0, blocking=True)
  ct.AddSub('circle', 'circle', std_msgs.msg.Float64MultiArray, lambda data: callback(data))
  time.sleep(15)
  
  
  
