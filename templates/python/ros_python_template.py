#!/usr/bin/env python
# Author:

# pylint: disable=C0103

# Description

import sys
import rospy


# global variables
current_ = None


# callback functions
# ========================================
def cb_function(data):
    ''' does whatever your callback should do '''
    pass



# User-Defined Functions
# ========================================
def get_ros_param(name):
    ''' get ros param value if provided '''
    if not rospy.has_param(name):
        rospy.logerr('Error: expected ' + str(name) + ' parameter to be set.')
        sys.exit(1)
    return rospy.get_param(name)


# ========================================
def main_loop():
    ''' main loop '''
    rospy.init_node('node_name', anonymous=True)

    # publishers
    pub = rospy.Publisher('topic_name', topic_type, queue_size=1)

    # subscribers
    rospy.Subscriber('/topic_name', topic_type, cb_function)

    # get ROS parameters from launch file
    launch_parameter = get_ros_param('~launch_parameter')

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():

        # main code

        # publish updated list
        pub.publish()
        rate.sleep()


# ============================
if __name__ == '__main__':
    try:
        main_loop()
    except rospy.ROSInterruptException:
        pass
