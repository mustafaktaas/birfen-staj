#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

def get_key():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def turtles_controller():
    rospy.init_node('turtles_controller_node', anonymous=True)
    pub_cmd_vel1 = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    pub_cmd_vel2 = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(10)  # Hareket hızı (10 Hz olarak ayarlandı)

    while not rospy.is_shutdown():
        key = get_key()
        move_cmd1 = Twist()
        move_cmd2 = Twist()

        if key == 'w':
            move_cmd1.linear.x = 2.0  # İleri doğru hız turtle1
        elif key == 's':
            move_cmd1.linear.x = -2.0  # Geri doğru hız turtle1
        elif key == 'a':
            move_cmd1.angular.z = 1.0  # Sağa dönme hızı turtle1
        elif key == 'd':
            move_cmd1.angular.z = -1.0  # Sola dönme hızı turtle1
        elif key == 'ı':
            move_cmd2.linear.x = 2.0  # İleri doğru hız turtle2
        elif key == 'k':
            move_cmd2.linear.x = -2.0  # Geri doğru hız turtle2
        elif key == 'j':
            move_cmd2.angular.z = 1.0  # Sağa dönme hızı turtle2
        elif key == 'l':
            move_cmd2.angular.z = -1.0  # Sola dönme hızı turtle2

        pub_cmd_vel1.publish(move_cmd1)
        pub_cmd_vel2.publish(move_cmd2)

        rate.sleep()

if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    try:
        turtles_controller()
    except rospy.ROSInterruptException:
        pass
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
