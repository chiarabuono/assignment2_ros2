#! /usr/bin/env python

import rclpy
from rclpy.node import Node
from rclpy.exceptions import ParameterNotDeclaredException
from rcl_interfaces.msg import ParameterType
from std_msgs.msg import String

# import rclpy.node

class RobotController(Node):

    def __init__(self):
        super().__init__('robot_controller')
               
       

# one node capable of moving the robot around in the simulation environment
def main(args=None):

    #init the node
    rclpy.init(args=args)
    robot_controller = RobotController()

    
    rclpy.spin(robot_controller)
    robot_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()