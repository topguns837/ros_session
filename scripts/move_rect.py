#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_straight(velocity_publisher, speed, duration):
    vel_msg = Twist()
    vel_msg.linear.x = speed
    vel_msg.angular.z = 0.0

    start_time = rospy.Time.now().to_sec()
    while rospy.Time.now().to_sec() - start_time < duration and not rospy.is_shutdown():
        velocity_publisher.publish(vel_msg)
    
    vel_msg.linear.x = 0.0
    velocity_publisher.publish(vel_msg)

def turn(velocity_publisher, angular_speed, duration):
    vel_msg = Twist()
    vel_msg.linear.x = 0.0
    vel_msg.angular.z = angular_speed

    start_time = rospy.Time.now().to_sec()
    while rospy.Time.now().to_sec() - start_time < duration and not rospy.is_shutdown():
        velocity_publisher.publish(vel_msg)
    
    vel_msg.angular.z = 0.0
    velocity_publisher.publish(vel_msg)

def move_turtle_rectangle():
    rospy.init_node('move_turtle_rectangle_node', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Speeds and durations for straight movement and turning
    straight_speed = 1.0  # Adjust as needed
    long_side_duration = 3.0  # Duration for long side
    short_side_duration = 1.5  # Duration for short side
    turn_speed = 0.5  # Adjust for 90-degree turn
    turn_duration = 3.14 / (2 * turn_speed)  # Duration for 90 degrees turn

    for _ in range(2):
        move_straight(velocity_publisher, straight_speed, long_side_duration)  # Move long side
        turn(velocity_publisher, turn_speed, turn_duration)  # Turn 90 degrees
        move_straight(velocity_publisher, straight_speed, short_side_duration)  # Move short side
        turn(velocity_publisher, turn_speed, turn_duration)  # Turn 90 degrees

if __name__ == '__main__':
    try:
        move_turtle_rectangle()
    except rospy.ROSInterruptException:
        pass

