#!/usr/bin/env python

# pylint: disable=C0103

import numpy as np
import matplotlib.pyplot as plt

def main_loop():
    ''' main loop '''
    x = np.array([-86.402987755093932,
                  -73.924180414808106,
                  -58.921926494117933,
                  -23.128262125495944,
                  -25.684088174988013])

    y = np.array([82.270417678205405,
                  85.189969184413087,
                  83.718633357689015,
                  73.404369198821257,
                  43.025271933508662])

    # sol = np.array([-22.7929225141, 77.3902878313])
    sol = np.array([-23.4636017369, 69.4184505663])

    plt.plot(x, y)
    plt.scatter(sol[0], sol[1], s=30)
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main_loop()
