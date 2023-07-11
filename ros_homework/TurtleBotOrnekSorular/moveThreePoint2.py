#!/usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseActionGoal
from std_msgs.msg import Header

def movetoGoal(x, y):
    pub = rospy.Publisher('/move_base/goal', MoveBaseActionGoal, queue_size=10)

    goal = MoveBaseActionGoal()
    goal.goal.target_pose.header = Header()
    goal.goal.target_pose.header.frame_id = 'map'
    goal.goal.target_pose.pose.position.x = x
    goal.goal.target_pose.pose.position.y = y
    goal.goal.target_pose.pose.orientation.w = 1.0

    rospy.sleep(1)
    pub.publish(goal)

if __name__ == '__main__':
    rospy.init_node('turtlebot_goal_publisher')

    # Üç adet hedef konumu belirleyin
    goals = [
        (2, 2),
        (3, 3),
        (1, 4)
    ]

    rate = rospy.Rate(0.1)  # Hedefler arasında geçiş hızı (Hz)

    for goal in goals:
        x, y = goal
        movetoGoal(x, y)
        rate.sleep(2)

    rospy.spin()