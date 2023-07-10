#!/usr/bin/env python

import rospy 
from sensor_msgs.msg import LaserScan 
from geometry_msgs.msg import Twist 

def callback(dt):
    print ('-------------------------------------------')
    print ('Range data at 0 deg:   {}'.format(dt.ranges[0]))
    print ('Range data at 15 deg:  {}'.format(dt.ranges[15]))
    print ('Range data at 345 deg: {}'.format(dt.ranges[345]))
    print ('-------------------------------------------')
    thr1 = 0.8 
    thr2 = 0.8
    if dt.ranges[0]>thr1 and dt.ranges[15]>thr2 and dt.ranges[345]>thr2: 
        move.linear.x = 0.5 
        move.angular.z = 0.0 
    else:
        move.linear.x = 0.0 
        move.angular.z = 0.5
        if dt.ranges[0]>thr1 and dt.ranges[15]>thr2 and dt.ranges[345]>thr2:
            move.linear.x = 0.5
            move.angular.z = 0.0
    pub.publish(move) 

if __name__ == '__main__':
    move = Twist() 
    rospy.init_node('obstacle_avoidance_node') 
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)  
    sub = rospy.Subscriber("/scan", LaserScan, callback)  
    rospy.spin() 
