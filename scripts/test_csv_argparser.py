#!/usr/bin/env python3

# system includes
import sys
import argparse

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
    csv_obj.print_contents()
    column_data = csv_obj.get_column_data(args.column_name)
    print("-- Column data: {}".format(column_data))


if __name__ == '__main__':
    sys.exit(main())
