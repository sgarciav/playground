#!/usr/bin/env python3

# system includes
import csv
import pandas

class ManipulateCSVFile():
    def __init__(self, filename, verbose = False):
        self.filename = filename
        self.verbose = verbose


    def print_contents(self):
        ''' print the contents of the csv file '''
        if self.verbose:
            print("-- Contents of the csv file: {}".format(self.filename))
        # open the CSV file
        with open(self.filename, mode = 'r') as file:
            # reading the CSV file
            csv_file = csv.reader(file)
            for lines in csv_file:
                print(lines)


    def get_column_data(self, column_name):
        ''' return the contents in the column as a numpy array - return False if it doesn't exist '''
        # check if the column exists in the current file
        all_data = pandas.read_csv(self.filename)
        if column_name not in all_data.columns:
            print("-- ERROR! Column {} not found in {}".format(column_name, self.filename))
            return False

        # get the column data
        df = pandas.read_csv(self.filename, usecols=[column_name])
        if self.verbose:
            print("-- Column {} from {} obtained successfuly".format(column_name, self.filename))

        # convert panda data frame to numpy array
        column_data_array = df.to_numpy()
        return column_data_array
