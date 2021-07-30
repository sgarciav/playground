#!/usr/bin/env python3

# system includes
import csv
import pandas
import os.path

class ManipulateCSVFile():
    def __init__(self, filename, verbose = False):
        self.filename = filename
        self.verbose = verbose


    def checkFile(self, header = None):
        ''' return False if file does not exist '''
        exists = True
        if not os.path.isfile(self.filename):
            if self.verbose:
                print("-- WARNING! File {} does not exist.".format(self.filename))
            exists = False
        # if file doesn't exist, should we create it?
        if not exists and header is not None:
            if self.verbose:
                print("-- Creating new file ({}) with header: {}".format(self.filename, header))
            self.appendRow(header)
            exists = True
        return exists


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


    def getColumnData(self, column_name):
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


    def getColumnNames(self):
        ''' return an array containing the name of all the columns '''
        all_data = pandas.read_csv(self.filename)
        return all_data.columns


    def getNumberOfColumns(self):
        ''' return the number of columns '''
        if self.verbose:
            print("-- Determinig the number of columns")
        all_data = pandas.read_csv(self.filename)
        num_cols = len(all_data.columns)
        return num_cols


    # def createFile(self, header):
    #     ''' create the file with the provided header '''
    #     with open(self.filename, 'wb') as csvfile:
    #         writer = csv.writer(csvfile, delimiter=',')



    def appendRow(self, row):
        ''' append the input row at the end of the file '''
        if self.verbose:
            print("-- Writing row {} to file {}".format(row, self.filename))
        with open(self.filename, "a") as f:
            writer = csv.writer(f)
            writer.writerow(row)
