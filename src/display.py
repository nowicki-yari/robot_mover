#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


def callback(data):
    rospy.loginfo("movement: " + str(data.linear.x))


def listener():
    rospy.init_node('display', anonymous=True)
    rospy.Subscriber("cmd_vel", Twist, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()