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
                        help='Relative path to the CSV to manipulate.')
    args = parser.parse_args()

    # create the CSV object
    csv_obj = ManipulateCSVFile.ManipulateCSVFile(args.filename, True)
    csv_obj.print_contents()


if __name__ == '__main__':
    sys.exit(main())
