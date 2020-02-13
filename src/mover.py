#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


def move():
    m = 2
    rospy.init_node('mover')
    publisher = rospy.Publisher('cmd_vel', Twist)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = m
        publisher.publish(twist)
        rate.sleep()


if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass
