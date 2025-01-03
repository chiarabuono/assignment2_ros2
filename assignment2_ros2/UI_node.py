#! /usr/bin/env python

import rclpy
from rclpy.node import Node
from rclpy.exceptions import ParameterNotDeclaredException
from rcl_interfaces.msg import ParameterType
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

# import rclpy.node

class RobotController(Node):

    def __init__(self):
        super().__init__('robot_controller')

        self.frequency_move_robot = 0.1
    
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer_move = self.create_timer(self.frequency_move_robot, self.move_robot)

        self.linear_x = 0.0
        self.linear_y = 0.0
        self.angular_z = 0.0

        self.time_stop = 1.0
        self.time_moving = 0.0
        
           
    def selectVelocity(self, velocityName):
        velocity = 0

        while True:
            try:
                velocity = float(input(f"{velocityName} Choose the velocity of the robot: "))
                return velocity
            except ValueError:
                print("Value not accetable. Digit a number.", end=" ")
    
    def update_velocity(self):
        self.time_moving = 0.0

        velocityChosen = Twist() 
        self.publisher_.publish(velocityChosen)

        self.linear_x = self.selectVelocity("[linear velocity x]")
        self.linear_y = self.selectVelocity("[linear velocity y]")
        self.angular_z = self.selectVelocity("[angular velocity z]")
    
    def move_robot(self):
        velocityChosen = Twist()

        velocityChosen.linear.x = self.linear_x
        velocityChosen.linear.y = self.linear_y
        velocityChosen.angular.z = self.angular_z      

        self.publisher_.publish(velocityChosen)
        self.time_moving += self.frequency_move_robot
        print(f"Publish velocity {self.time_moving=}")

        if self.time_moving >= self.time_stop:
            self.update_velocity()
        

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