#!/usr/bin/env python3

# system includes
import sys
import argparse

import numpy as np
import matplotlib.pyplot as plt

# local includes
import ManipulateCSVFile

def main():
    parser = argparse.ArgumentParser(description = 'Main file to test the CSV class and argparser.')
    parser.add_argument('-f', '--filename',
                        type=str,
                        default=None,
                        help='Absolute or relative path to the CSV to manipulate.')
    parser.add_argument('-c', '--column-name',
                        type=str,
                        default="a",
                        help='Name of the column of interest.')
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        default=False,
                        help='Print debug messages.')
    args = parser.parse_args()

    # create the CSV object
    csv_obj = ManipulateCSVFile.ManipulateCSVFile(args.filename, args.verbose)
    if args.verbose:
        csv_obj.print_contents()
    column_data = csv_obj.get_column_data(args.column_name)
    if args.verbose:
        print("-- Column data: {}".format(column_data))

    # plot
    x = []
    for i in range(0,len(column_data)):
        x.append(i)
    x = np.array(x)

    plt.plot(x, column_data)
    # plt.plot(x2, y2, 'red')
    plt.grid()
    plt.show()




if __name__ == '__main__':
    sys.exit(main())
