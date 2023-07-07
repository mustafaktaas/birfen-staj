#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def odom_callback(msg):
    rospy.loginfo("Position (x, y, z): %.2f, %.2f, %.2f" % (msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z))
    rospy.loginfo("Orientation (x, y, z, w): %.2f, %.2f, %.2f, %.2f" % (msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w))

rospy.init_node('odom_subscriber')
rospy.Subscriber('/odom', Odometry, odom_callback)
rospy.spin()
