#!/usr/bin/env python
''' Author: Sergio Garcia-Vergara '''

# Plot distance between uavs as a function of time.

# pylint: disable=C0103

import matplotlib.pyplot as plt
import rospy
from std_msgs.msg import Float64

# global variables
wpx_ = None
wpy_ = None
dist_TH_ = 5


# callback functions
# ========================================
def distance_callback(data):
    ''' coordinates of the next waypoint '''
    global wpy_
    # wpx_ = data.data
    wpy_ = data.data


def plotme(t):
    ''' add the next point to the plot '''
    if wpy_ is not None:
        plt.scatter(t, wpy_, color='red')
        plt.scatter(t, dist_TH_, color='blue')

    plt.pause(0.05)

    rospy.loginfo("dist: %.2f", wpy_)


# ========================================
def main_loop():
    ''' main loop '''

    # initialize ROS node and publisher
    rospy.init_node('sergiotest_plot_distance', anonymous=True)

    # subscribers
    rospy.Subscriber('/UAV1/sergiotopic', Float64, distance_callback)

    # initialize plot
    fig = plt.figure()
    fig.suptitle('Distance Bteween UAVs', fontsize=14, fontweight='bold')
    plt.grid()

    # continue while ROS is working
    t = 0
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        t += 1
        plotme(t)
        rate.sleep()

# ----------------------

if __name__ == '__main__':
    try:
        main_loop()
    except rospy.ROSInterruptException:
        pass
