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
    'Health' : 0,
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

    # Clean the data: filter out empty strings AND 'nan' values caused by empty CSV rows
    raw_data = [str(x).strip() for x in column_data.tolist() if str(x).strip() and str(x).strip().lower() != 'nan']

    # print(raw_data)

    total_spending = 0
    current_name = ""

    for item in raw_data:
        item = item[2:-2] # Remove brakets
        try:
            # If the item can be cast to a float, it's the price.
            # This triggers the end of the current record.
            price = float(item)

            total_spending += price

            counted = False
            for cat in categories:
                if cat in current_name:
                    categories[cat] += price
                    counted = True
                    break

            if not counted:
                print(f'Item: ({current_name}) not counted')

            # Reset name for the next transaction
            current_name = ""

        except ValueError:
            # If it's not a float, it's either a date or a description.
            # We ignore short date strings (e.g., "3/16") and grab the first description line.
            if not current_name and not (len(item) <= 5 and '/' in item):
                current_name = item

    # Print results
    print('')
    print(f'Total travel spend: ${total_spending:.2f}')
    for cat, amount in categories.items():
        print(f'{cat}: ${amount:.2f}')

if __name__ == '__main__':
    sys.exit(main())
