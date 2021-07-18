#!/usr/bin/env python3

# system includes
import csv

class ManipulateCSVFile():
    def __init__(self, filename, verbose = False):
        self.filename = filename
        self.verbose = verbose

    def print_contents(self):
        ''' print the contents of the csv file '''
        if (self.verbose):
            print("-- Contents of the csv file:")
        # open the CSV file
        with open(self.filename, mode = 'r') as file:
            # reading the CSV file
            csv_file = csv.reader(file)

            for lines in csv_file:
                print(lines)
