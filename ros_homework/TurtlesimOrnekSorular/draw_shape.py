#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Color

def draw_shape():
    rospy.init_node('draw_shape_node', anonymous=True)
    pub_cmd_vel = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    pub_bg_color = rospy.Publisher('/turtle1/color_bg', Color, queue_size=10)
    rate = rospy.Rate(10)

    shape = input("Çizilecek şekli seçin (kare, yuvarlak, üçgen): ")

    move_cmd = Twist()

    if shape == "kare":
        for _ in range(4):
            move_cmd.linear.x = 2.0  # İleri doğru hız
            move_cmd.angular.z = 0.0  # Dönme hızı
            pub_cmd_vel.publish(move_cmd)
            rospy.sleep(2)
            move_cmd.linear.x = 0.0 
            pub_cmd_vel.publish(move_cmd)
            rospy.sleep(1)
            move_cmd.angular.z = 1.5708  # 90 derece dönme hızı (pi/2)
            pub_cmd_vel.publish(move_cmd)
            rospy.sleep(1)
    elif shape == "yuvarlak":
         for _ in range(7):
            move_cmd.linear.x = 2.0  
            move_cmd.angular.z = 1.0  
            pub_cmd_vel.publish(move_cmd)
            rospy.sleep(1.0)
    elif shape == "üçgen":
        for _ in range(3):
            move_cmd.linear.x = 2.0  
            move_cmd.angular.z = 0.0  
            pub_cmd_vel.publish(move_cmd)
            rospy.sleep(2.0)
            move_cmd.linear.x = 0.0  
            pub_cmd_vel.publish(move_cmd)
            rospy.sleep(1.0)
            move_cmd.angular.z = 2.0944  # 120 derece dönme hızı (2*pi/3)
            pub_cmd_vel.publish(move_cmd)
            rospy.sleep(1.0)

    # Arkaplan rengini değiştirin
    bg_color = Color()
    bg_color.r = 255
    bg_color.g = 255
    bg_color.b = 255
    pub_bg_color.publish(bg_color)

if __name__ == '__main__':
    try:
        draw_shape()
    except rospy.ROSInterruptException:
        pass
