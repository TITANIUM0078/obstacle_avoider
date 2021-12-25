import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import numpy as np
from tf.transformations import euler_from_quaternion

class obstacke_avoider:



    def odom_callback(data):
     global pose
    x  = data.pose.pose.orientation.x
    y  = data.pose.pose.orientation.y
    z = data.pose.pose.orientation.z
    pose = [data.pose.pose.position.x, data.pose.pose.position.y, euler_from_quaternion([x,y,z,w])[2]]

    
    def obstackle_avoidense() :
        pass



    def goto(dest_x, dest_y):
        pass
    
    
    
    def control_loop():

        rospy.Subscriber('/odom', Odometry, odom_callback)


