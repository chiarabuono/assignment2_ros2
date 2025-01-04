#! /usr/bin/env python

import rclpy
from rclpy.node import Node
from rclpy.exceptions import ParameterNotDeclaredException
from rcl_interfaces.msg import ParameterType
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

class RobotController(Node):

    def __init__(self):
        super().__init__('robot_controller')

        # publisher that publishes the velocity of the robot /cmd_vel topic    
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer_move = self.create_timer(0.1, self.move_robot)

        # subscriber that subscribes to the odom message of the odom topic
        self.subscriber_ = self.create_subscription(Odometry, '/odom', self.listener, 10)

    def move_robot(self):
        velocityChosen = Twist()
        x_pos = self.odom.pose.pose.position.x 
        # y_pos = self.odom.pose.pose.position.y

        angular_z = 0.0
        linear_x = 1.0
        
        if x_pos > 9.0: angular_z = 1.0
        elif x_pos < 2.0: angular_z = -1.0

        velocityChosen.linear.x = linear_x
        velocityChosen.angular.z = angular_z      

        self.publisher_.publish(velocityChosen)


    def listener(self, msg):
        self.odom = msg
        

# one node capable of moving the robot around in the simulation environment
def main(args=None):

    #init the node
    rclpy.init(args=args)
    robot_controller = RobotController()

    try:
        rclpy.spin(robot_controller)
    except KeyboardInterrupt:
        print("\nExiting.")
    finally:
        robot_controller.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()