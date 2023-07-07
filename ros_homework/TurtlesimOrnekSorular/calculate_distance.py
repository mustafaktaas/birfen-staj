import rospy
import tf
import math

# ROS düğümünü başlat
rospy.init_node('engel_takip')

def main():
    listener = tf.TransformListener()

    # Engellerin konumlarını belirleyin
    cop_kutusu_konumu = [5, 5, 0]
    masa_konumu = [5, 8, 0]

    while not rospy.is_shutdown():
        try:
            # Robotun konumunu dinle
            (trans, rot) = listener.lookupTransform('/world', '/base_link', rospy.Time(0))
            
            # Robotun konumu
            robot_konumu = [trans[0], trans[1], trans[2]]
            
            # Robotun konumuyla engellerin konumlarını karşılaştır
            cop_kutusu_mesafe = mesafe_hesapla(robot_konumu, cop_kutusu_konumu)
            masa_mesafe = mesafe_hesapla(robot_konumu, masa_konumu)

            # En yakın engeli belirle
            if cop_kutusu_mesafe < masa_mesafe:
                en_yakin_engel = "çöp kutusu"
                en_yakin_engel_mesafe = cop_kutusu_mesafe
            else:
                en_yakin_engel = "masa"
                en_yakin_engel_mesafe = masa_mesafe

            # Çıktıyı ROS loglarına yazdır
            rospy.loginfo("Robot, en yakın engel olarak %s uzaklığı %s birimdir.", en_yakin_engel, en_yakin_engel_mesafe)

            rospy.sleep(1.0)  # Yenileme hızı
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

def mesafe_hesapla(konum1, konum2):
    # Euclidean mesafesi hesaplama
    x1, y1, _ = konum1
    x2, y2, _ = konum2
    mesafe = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return mesafe

if __name__ == '__main__':
    main()
    rospy.spin()  # ROS döngüsünü çalıştır
