#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from math import atan2, degrees

def odom_callback(msg):
    # Hedef konumu belirleyin
    goal_x = 3.0
    goal_y = 3.0

    # TurtleBot'un mevcut konumunu ve yönelimini alın
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    orientation = msg.pose.pose.orientation

    # Quaternion'i Euler açılarına dönüştürün
    euler_angles = euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])

    # TurtleBot'un mevcut yönelim açısını hesaplayın
    current_yaw = degrees(euler_angles[2])

    # Hedefe yönelik açıyı hesaplayın
    target_yaw = atan2(goal_y - y, goal_x - x)
    target_yaw_degrees = degrees(target_yaw)

    # Hedefe yönelmek için dönüş açısını hesaplayın
    turn_angle = target_yaw_degrees - current_yaw

    # Dönüş açısı sınırlarını [-180, 180] aralığında tutun
    if turn_angle > 180:
        turn_angle -= 360
    elif turn_angle < -180:
        turn_angle += 360

    # Dönüş açısına göre TurtleBot'u hareket ettirin
    if abs(turn_angle) > 5:  # Hedefe doğru dönme açısı eşik değeri
        # Dönme hareketi
        move.linear.x = 0.0
        move.angular.z = turn_angle * 0.01  # Dönme hızını ayarlayın
    else:
        # İleri hareket
        move.linear.x = 0.2  # İleri hızını ayarlayın
        move.angular.z = 0.0

    pub.publish(move)  # Hareket komutunu yayınlayın

if __name__ == '__main__':
    rospy.init_node('turtlebot_goal_omni_drive')

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/odom', Odometry, odom_callback)

    move = Twist()  # Hareket mesajı nesnesini oluşturun

    rospy.spin()
