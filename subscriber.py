#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32

def callback(data):
    #rospy.loginfo("I heard %d",data.data) #, "from", rospy.get_caller_id())
    print( rospy.get_name() + ': data: ' + str(data.data))

def subscriber():
    rospy.init_node('subscriber')
    rospy.Subscriber("/topic", Int32, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    subscriber()
