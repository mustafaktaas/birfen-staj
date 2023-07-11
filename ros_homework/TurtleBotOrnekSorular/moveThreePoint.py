#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point

# Bu yöntem robotun hedef konuma gitmesini sağlar
def move_to_goal(xGoal, yGoal):

   # move_base sunucusuna istek göndermek için bir SimpleActionClient oluşturun
   ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

   # Hareket sunucusunun hazır olmasını bekleyin
   while not ac.wait_for_server(rospy.Duration.from_sec(5.0)):
       rospy.loginfo("Hareket sunucusunun başlaması bekleniyor")

   goal = MoveBaseGoal()

   # Çerçeve parametrelerini ayarlayın
   goal.target_pose.header.frame_id = "map"
   goal.target_pose.header.stamp = rospy.Time.now()

   # Hedefe doğru hareket edin
   goal.target_pose.pose.position = Point(xGoal, yGoal, 0)
   goal.target_pose.pose.orientation.x = 0.0
   goal.target_pose.pose.orientation.y = 0.0
   goal.target_pose.pose.orientation.z = 0.0
   goal.target_pose.pose.orientation.w = 1.0

   rospy.loginfo("Hedef konuma gidiliyor...")
   ac.send_goal(goal)

   ac.wait_for_result(rospy.Duration(5))

   if ac.get_state() == GoalStatus.SUCCEEDED:
       rospy.loginfo("Hedefe ulaşıldı")
       return True
   else:
       rospy.loginfo("Robot hedefe ulaşamadı")
       return False

if __name__ == '__main__':
   rospy.init_node('map_navigation', anonymous=False)
   points = [
       [-2.02880191803, 4.02200937271],  # Nokta 1
       [1.0, 1.0],                        # Nokta 2
       [-1.5, -2.0]                       # Nokta 3
   ]

   print('Hedefe gidiliyor...')
   while True:
       for point in points:
           x_goal, y_goal = point
           move_to_goal(x_goal, y_goal)
   rospy.spin()