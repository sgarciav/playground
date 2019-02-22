#!/usr/bin/env python

# pylint: disable=C0103

import numpy as np
# from array_lists import array100
import array_lists

def main_loop():
    ''' main loop '''
    main_array = []
    for i in range(0,10):
        main_array.append(i)

    print main_array
    # print array100()
    print array_lists.array100()

if __name__ == '__main__':
    main_loop()
