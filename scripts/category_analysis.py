#!/usr/bin/env python3

# system includes
import sys
import argparse

import numpy as np
# import matplotlib.pyplot as plt

# local includes
import ManipulateCSVFile

categories = {
    'Flight' : 0,
    'Auto' : 0,
    'Hotel' : 0,
    'Shopping' : 0,
    'Entertainment' : 0,
    'Misc' : 0,
    'Food' : 0,
}

def main():
    parser = argparse.ArgumentParser(description = 'Main file to test the CSV class and argparser.')
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        default=False,
                        help='Print debug messages.')
    args = parser.parse_args()

    filename = '~/Downloads/travel.csv'
    column_name = 'travel'

    csv_obj = ManipulateCSVFile.ManipulateCSVFile(filename, False)
    column_data = csv_obj.getColumnData(column_name)

    # Order of data: Date, Name, Price
    grouped_list = list(zip(*[iter(column_data.tolist())]*3))

    total_spending = 0
    for kv in grouped_list:
        name = str(kv[1])
        price = float(kv[2][0])
        total_spending += price

        counted = False
        for cat in categories:
            if cat in name:
                categories[cat] += price
                counted = True
                break

        if not counted:
            print(f'Item ({name}) not counted')

    # Print results
    print('')
    print(f'Total travel spend: ${total_spending}')
    for c in categories.items():
        print(c)

if __name__ == '__main__':
    sys.exit(main())
