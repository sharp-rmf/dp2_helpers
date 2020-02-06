#!/bin/bash

cd ~/dp2_ws && rm -rf build log install && source /opt/ros/eloquent/setup.bash && colcon build
#ssh -t ubuntu@magni1.local "cd magni_ws && source /opt/ros/melodic/setup.bash && build devel logs &&catkin build"
ssh -t ubuntu@magni2.local "cd magni_ws && source /opt/ros/melodic/setup.bash && rm -rf build devel logs && catkin build"
ssh -t ubuntu@magni3.local "cd magni_ws && source /opt/ros/melodic/setup.bash && rm -rf build devel logs && catkin build"
#ssh -t ubuntu@magni4.local "cd magni_ws && source /opt/ros/melodic/setup.bash && rm -rf build devel logs && catkin build"
