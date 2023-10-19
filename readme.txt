README - TortoiseBotProMax Autonomous Navigation

This repository contains code and instructions for autonomous navigation of a TortoiseBotProMax using various algorithms in ROS. 
Below, you will find information about the algorithms used, references, completed tasks, and commands to run.

Algorithms Used:

1. Aruco Scanning using OpenCV: Aruco marker detection is used for robot localization.
2. Gmapping for Map Generation: Gmapping is employed to create a map of the environment.
3. MoveBase for Navigation: MoveBase is used for robot navigation to predefined waypoints.
4. AMCL for Localization: AMCL (Adaptive Monte Carlo Localization) is used for precise localization of the robot.
5. base_local_planner for Path Planning: The DWA (Dynamic Window Approach) planner is utilized for path planning and obstacle avoidance.

References:
- ROS Wiki - Setting up the Navigation Stack for TurtleBot: http://wiki.ros.org/action/fullsearch/turtlebot_navigation/Tutorials/Setup%20the%20Navigation%20Stack%20for%20TurtleBot?action=fullsearch&context=180&value=linkto%3A%22turtlebot_navigation%2FTutorials%2FSetup+the+Navigation+Stack+for+TurtleBot%22
- GitHub - ROS Course Part 2 - navigate_goal.py: https://github.com/aniskoubaa/ros_course_part2/blob/master/src/topic03_map_navigation/navigate_goal.py

Tasks Completed:
- Mapping (Manually): A map of the environment has been created manually using Gmapping.
- Aruco Marker Scanning Achieved: The robot can detect and scan IDs of Aruco markers in the environment.
- Waypoint poses calculated: After scanning ID, rostopic echo was used to find the pose coordinates and save to a text file.
- Autonomous Navigation Package and Launch files created: Autonomous navigation setup has been successfully configured.
- Path Planning to Waypoints Done: The robot can plan paths to waypoints of aruco poses.
- Obstacle Avoidance Done: The robot's footprint size has been increased to avoid obstacles and corners in its path.
- Navigation to Waypoints: The robot navigates to the sequence of waypoints and pauses for a duration of 30 s.
- Speed of robot has been increased to reduce time of autonomous navigation.

Commands to Run:
After bringing up Gazebo model and RViz using given launch files,
cd catkin_ws/src
rosrun map_server map_server map.yaml
roslaunch tortoisebotpromax_navigation amcl.launch
roslaunch tortoisebotpromax_navigation move_base.launch
python move_to_waypoints.py
