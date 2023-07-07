#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def publish_cmd_vel():
    rospy.init_node('cmd_vel_publisher', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # Yayın hızı (10 Hz olarak ayarlandı)

    while not rospy.is_shutdown():
        cmd_vel_msg = Twist()
        cmd_vel_msg.linear.x = 0.2  # Lineer hız
        cmd_vel_msg.angular.z = 0.5  # Açısal hız

        pub.publish(cmd_vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_cmd_vel()
    except rospy.ROSInterruptException:
        pass
