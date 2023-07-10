#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty

def move_and_stop(distance):
    rospy.init_node('turtlebot3_move_and_stop')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    vel_msg = Twist()
    distance_moved = 0

    while distance_moved < distance:
        # İleri hareket
        vel_msg.linear.x = 0.2  # İleri hızı (m/s)
        vel_msg.angular.z = 0  # Dönüş hızı
        pub.publish(vel_msg)
        rate.sleep()
        distance_moved += abs(vel_msg.linear.x) * 0.1  # Örnek süre (sn) * hız (m/s)

    # Durma işlemi
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    pub.publish(vel_msg)
    """
    try:
        reset_simulation = rospy.ServiceProxy('/gazebo/reset_world', Empty)
        reset_simulation()
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)
    """

if __name__ == '__main__':
    try:
        distance_to_move = 1.0  # Hedef mesafe (metre)
        move_and_stop(distance_to_move)
    except rospy.ROSInterruptException:
        pass
