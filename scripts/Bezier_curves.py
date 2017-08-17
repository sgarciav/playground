#!/usr/bin/env python

# pylint: disable=C0103

# https://github.com/dhermes/bezier

import numpy as np
import bezier
import matplotlib.pyplot as plt

def main_loop():
    ''' main loop '''
    nodes = np.array([[0., 0.],
                      [0.5, 1.0],
                      [0.5, 3.0],
                      [1.0, 0.]])
    curve = bezier.Curve(nodes, degree=2)

    num_points = 10
    vals = np.linspace(0.0, 1.0, num_points)
    pts = curve.evaluate_multi(vals)
    print str(pts)

    x = []
    y = []
    for n in nodes:
        x.append(n[0])
        y.append(n[1])

    ax = curve.plot(num_pts=100)
    for p in pts:
        plt.scatter(p[0], p[1], s=20)
    plt.plot(x, y, 'r--')
    plt.axis('equal')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main_loop()
