#!/usr/bin/env python

# pylint: disable=C0103

import math
import numpy as np
# import gtri_pkg.angle_fncts
import matplotlib.pyplot as plt

def shift_90deg():
    ''' shift start point 90 deg to right of lane '''
    start = np.array([0, 0])
    end = np.array([-1, -1])

    d = end - start
    yaw = math.atan2(d[1], d[0])
    print yaw * 180 / np.pi

    h = np.linalg.norm(d) / 2
    a = start[0] + h * math.cos(np.pi / 2.0 - yaw)
    b = start[1] - h * math.sin(np.pi / 2.0 - yaw)

    x = np.array([a, start[0], end[0]])
    y = np.array([b, start[1], end[1]])
    print x
    print y

    plt.scatter(x, y, s=35)
    plt.plot(x, y, 'r--')
    plt.axis('equal')
    plt.grid()
    plt.show()


def plot_points():
    ''' just plot some points '''

    # points = np.array([[-86.84286567, 84.22144495, 0.],
    #                    [-73.72183773, 87.17970722, 0.],
    #                    [-58.26575717, 85.60793, 0.],
    #                    [-23.12826213, 73.4043692, 0.],
    #                    [-23.31108483, 63.40604055, 0.],
    #                    [-23.68442244, 42.98870739, 0.]])

    points = np.array([[-86.40298776, 82.27041768],
                       [-73.92418041, 85.18996918],
                       [-58.92192649, 83.71863336],
                       [-23.12826213, 73.4043692],
                       [-23.96661115, 63.43957262],
                       [-25.68408817, 43.02527193]])

    x = []
    y = []
    for p in points:
        x.append(p[0])
        y.append(p[1])

    plt.scatter(x, y, s=35)
    plt.plot(x, y, 'r--')
    plt.axis('equal')
    plt.grid()
    plt.show()


def main_loop():
    ''' main loop '''

    shift_90deg()
    # plot_points()

if __name__ == '__main__':
    main_loop()
