#!/usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseActionGoal
from std_msgs.msg import Header

def  movetoGoal(x,y):
    pub = rospy.Publisher('/move_base/goal', MoveBaseActionGoal, queue_size=10)

    goal = MoveBaseActionGoal()
    # sor
    goal.goal.target_pose.header = Header()  # Yeni bir Header nesnesi oluşturun
    goal.goal.target_pose.header.frame_id = 'map'  # Hedef konumu harita koordinat sistemi üzerinde belirtilmelidir
    goal.goal.target_pose.pose.position.x = x  
    goal.goal.target_pose.pose.position.y = y  
    goal.goal.target_pose.pose.orientation.w = 1.0  # Hedefin yönelimi (quaternion)

    rospy.sleep(1)  
    pub.publish(goal) 

    
if __name__ == '__main__':
    rospy.init_node('turtlebot_goal_publisher')
    movetoGoal(6,4)
    rospy.spin()
