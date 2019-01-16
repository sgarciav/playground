#!/usr/bin/env python
''' Author: Sergio Garcia-Vergara '''

# Plot the altitude estimate output from the target pose estimator.

# pylint: disable=C0103

import matplotlib.pyplot as plt
import rospy
from gt_uav_msgs.msg import TrackConfidence

# global variables
altitude_ = None
max_alt_ = -1


# callback functions
# ========================================
def pose_estimate_callback(data):
    ''' coordinates of the next point to plot '''
    global altitude_
    altitude_ = data.pos_LLA[2]


def plotme(t):
    ''' add the next point to the plot '''
    global max_alt_

    if altitude_ is not None:
        plt.scatter(t, altitude_, color='red')
        if altitude_ > max_alt_:
            max_alt_ = altitude_
        rospy.loginfo("current max alt: %.2f", max_alt_)

    plt.pause(0.05)


# ========================================
def main_loop():
    ''' main loop '''

    # initialize ROS node and publisher
    rospy.init_node('sergiotest_plot_alt_estimate', anonymous=True)

    # subscribers
    rospy.Subscriber('/targ_pose_track_camera', TrackConfidence, pose_estimate_callback)

    # initialize plot
    fig = plt.figure()
    fig.suptitle('Altitude Estimate', fontsize=14, fontweight='bold')
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
