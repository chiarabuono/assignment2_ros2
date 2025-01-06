# Assignment 2 Research Track 1
This repository contains a ROS2 node that interact with the Gazebo environment and allows the robot to move around in the environment.
# Requirements
Before using the package, make sure you have ROS2 (any compatible version) installed. Additionally, you must have a working workspace to compile and run the package. If you do not already have a workspace, follow these steps to create a new one:
```
mkdir -p ~/ros2_ws/src
gedit ~/.bashrc
```
and add this line ```source /root/ros2_ws/install/local_setup.bash ``` to the bashrc file, where /root/ros2_ws is the path of the folder. Lastly, make sure that also this line of code are present 
```
source /opt/ros/foxy/setup.bash
source /usr/share/colcon_cd/function/colcon_cd.sh
```
Then, close and reopen the terminal to make the changes effective.
Make sure you have Gazebo installed as well, as it is required to run the simulation.
# Package installation
1.	Go inside the src folder ```cd ~/ros2_ws/src```
2.	Clone the repository into your workspace: ```git clone git@github.com:chiarabuono/assignment2_ros2.git```
3.	Clone the robot_urdf package into your workspace, as it contains the simulation environment used in this repository: ```git clone git@github.com:CarmineD8/robot_urdf.git```
4.	Build the workspace in the main folder:
```
cd ~/ros2_ws
colcon build
```
# How to Run the package
1.	Run the gazebo environment ```ros2 launch robot_urdf gazebo.launch.py```
2.	In a new terminal, run the node with ```ros2 run assignment2_ros2 robot_controller_node```
# Node description
robot_controller_node allows the robot to move forward within the simulation environment its direction based on its x-position, ensuring it remains within a predefined range (2.0 < x < 9.0).