#!/usr/bin/env python

# This node publishes a high-level trajectory for navigating from
# Point A to Point B. It requires that the OSM router service is running,
# as it uses that functionality for determining the navigation waypoints.
# It publishes the resulting trajectory to the waypoint handler and
# starts navigation control so that the vehicle immediately starts following
# the trajectory.

import matplotlib.pyplot as plt
import rospy
import sys
import time
from car_nav2d.srv import *
from std_msgs.msg import String
from geometry_msgs.msg import Pose
from yocs_msgs.msg import NavigationControl
from yocs_msgs.msg import Waypoint
from yocs_msgs.msg import Trajectory
from yocs_msgs.msg import TrajectoryList

# Get arguments.
if len(sys.argv) != 5:
    print('Usage: send_trajectory <latBegin> <lonBegin> <latEnd> <lonEnd> <robot_name>')
    sys.exit(1)
latBegin = float(sys.argv[1])
lonBegin = float(sys.argv[2])
latEnd = float(sys.argv[3])
lonEnd = float(sys.argv[4])

# initialize plot
fig = plt.figure()
fig.suptitle('Coordinates', fontsize=14, fontweight='bold')
plt.grid()

# Set up node and publishers.
rospy.init_node('send_trajectory', anonymous=True)
trajPub = rospy.Publisher('/trajectories', TrajectoryList, queue_size=1)
nav_ctrl = rospy.Publisher('/nav_ctrl', NavigationControl, queue_size=1)
time.sleep(3)

# Get trajectory from the OSM router.
rospy.wait_for_service('/osm_router')
osm_router = rospy.ServiceProxy('/osm_router', OsmRouter)
try:
    # Send routing request.
    req = OsmRouterRequest()
    req.begin.longitude = lonBegin
    req.begin.latitude = latBegin
    req.end.longitude = lonEnd
    req.end.latitude = latEnd
    response = osm_router(req)

    # Publish the trajectory.
    tl = TrajectoryList()
    traj = response.route
    TRAJ_NAME = 'main' # arbitrary
    traj.name = TRAJ_NAME
    tl.trajectories = [traj]
    trajPub.publish(tl)
    time.sleep(2)

    # Start navigation control.
    nc = NavigationControl()
    nc.control = NavigationControl.START
    nc.goal_name = TRAJ_NAME
    nav_ctrl.publish(nc)
except rospy.ServiceException as exc:
    print('Service did not process request: ' + str(exc))

# plot the waypoints
for wp in traj.waypoints:
    print wp.pose.position.x
    print wp.pose.position.y
    print ''
    plt.scatter(wp.pose.position.x, wp.pose.position.y)
