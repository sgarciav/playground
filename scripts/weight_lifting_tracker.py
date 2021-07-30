#!/usr/bin/env python3

# This script manipulates csv files that contains the 1RM progress for
# and plots the results. Each file contains a column pair (date vs
# weight). The script provides functionality for adding a new entry
# for a given exercise or add a new file to start keeping track of a
# new exercise.

# system includes
import os
import sys
import argparse
import matplotlib.pyplot as plt

# local includes
import ManipulateCSVFile

def main():
    parser = argparse.ArgumentParser(description = 'Keep track of the 1RM weight lifting for various exercises.')
    parser.add_argument('-e', '--exercise',
                        type=str,
                        default=None,
                        help='Name of the exercise to update (e.g., squat, bench, etc.)')
    parser.add_argument('-d', '--date',
                        type=str,
                        default=None,
                        help='Date at which the update was performed.')
    parser.add_argument('-w', '--weight',
                        type=int,
                        default=None,
                        help='1RM weight (in lbs) for the provided exercise name at the provided date.')
    parser.add_argument('-l', '--list-exercises',
                        action='store_true',
                        default=False,
                        help='Option to print list of available exercises. Nothing else happens.')
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        default=False,
                        help='Print debug messages.')
    args = parser.parse_args()

    # directory where all the exercise files live
    base_dir = "../test_files/weight_records/"

    # determine the number exercises available
    all_files = os.listdir(base_dir)
    num_exercises = len(all_files)
    if args.verbose:
        print("-- There are ({}) exercises available.".format(num_exercises))

    # list the available exercises
    if args.list_exercises or args.verbose:
        print("-- Availabe exercises:")
        for f in all_files:
            print(f[:-4])
    if args.list_exercises:
        return 1

    # sanity check
    if args.exercise is None:
        print("-- ERROR! An exercise name needs to be provided.")
        return 1

    # create the csv object and perform sanity check
    exercise_filename = args.exercise + ".csv"
    exercise_full_path = base_dir + exercise_filename
    csv_obj = ManipulateCSVFile.ManipulateCSVFile(exercise_full_path, args.verbose)
    header = ["date", "weight"] # if file doesn't exist, create it with this header
    success = csv_obj.checkFile(header)
    if not success:
        return 1

    # sanity check on date and weight inputs
    # TODO: check that the provided date is after the latest date in the file
    if args.date is None or args.weight is None:
        print("-- ERROR! date ({}) or weight ({}) missing input.".format(args.date, args.weight))
        return 1

    # update the exercise of interest
    if args.verbose:
        print("-- Updating exercise: {}".format(args.exercise))
    row = [args.date, args.weight]
    csv_obj.appendRow(row)



    # # setup the figure
    # fig, ax = plt.subplots(1, num_plots)

    # ax[0].plot("r","1s", data=s_orbitals)
    # ax[1].plot("r","2s", data=s_orbitals)
    # ax[2].plot("r","3s", data=s_orbitals)

    # for axis in ax:
    #     axis.set_xlabel("r")
    #     axis.set_ylabel("Weight 1RM [lbs]")
    #     axis.legend()

    # fig.tight_layout()


if __name__ == '__main__':
    sys.exit(main())
