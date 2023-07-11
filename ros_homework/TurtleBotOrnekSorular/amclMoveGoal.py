import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf.transformations import euler_from_quaternion
import math

def amcl_pose_callback(msg):
    # Hedef konumu belirleyin
    goal_x = 1.0
    goal_y = 2.0

    # TurtleBot'un mevcut konumunu alın
    current_x = msg.pose.pose.position.x
    current_y = msg.pose.pose.position.y

    # TurtleBot'un mevcut yönelim açısını alın
    orientation = msg.pose.pose.orientation
    _, _, yaw = euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])

    # Hedef konum ile mevcut konum arasındaki farkları hesaplayın
    diff_x = goal_x - current_x
    diff_y = goal_y - current_y

    # Hedefe doğru yönelme açısını hesaplayın
    target_angle = math.atan2(diff_y, diff_x)

    # Dönüş açısını hesaplayın
    turn_angle = target_angle - yaw

    # Dönme hızını ayarlayın
    angular_speed = 0.5  # Radyan/s
    turn_duration = abs(turn_angle / angular_speed)

    # Dönme hareketini gerçekleştirin
    if turn_angle > 0:
        move.angular.z = angular_speed
    else:
        move.angular.z = -angular_speed
    pub.publish(move)
    rospy.sleep(turn_duration)
    move.angular.z = 0.0
    pub.publish(move)

    # İleri hareketi gerçekleştirin
    move.linear.x = 0.2  # m/s
    pub.publish(move)
    rospy.sleep(1.0)  # Belirli bir süre ileri hareket ettirin
    move.linear.x = 0.0
    pub.publish(move)

if __name__ == '__main__':
    rospy.init_node('turtlebot_goal_amcl')

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, amcl_pose_callback)

    move = Twist()  # Hareket mesajı nesnesini oluşturun

    rospy.spin()
