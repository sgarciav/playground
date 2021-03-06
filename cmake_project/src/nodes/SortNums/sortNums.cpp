#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include<iostream>

#include <cmake_project/common/helper_functions.h>

using std::cout;
using std::endl;

int main (int argc, char *argv[]) {

    if (argc < 2) {
        cout << "ERROR: Provide as input, at least, one integer." << endl << endl;
        cout << "Use -h option to receive more detailed instructions." << endl;
        return 1;
    }

	// usage
	char msg[] = "USAGE: This script sorts a set of integers from minimum to maximum.\nNOTE: All inputs should be less than";
	sprintf(msg, "%s %d.", msg, allmax);
    std::string input_str = std::string(argv[1]);
	if (input_str.compare("-h") == 0) {
		printf("%s", msg);
		printSpace(2);
		return 0;
	}

    // amount of input numbers to sort
    int input_len = argc - 1;

    // read input numbers
    int i, array[input_len];
    for (i = 1; i <= input_len; i++) {
        array[i-1] = atoi(argv[i]);
    }

    // display original numbers
    printf("Original Numbers: \n===================\n");
    printArray(array, input_len);
    printSpace(2);

    // go through all input values
    int sorted[input_len], ind;
    for (i=0; i<input_len; i++) {
        // get index of minimum number in original array
        ind = getMinInd(array, input_len);

        // store minimum value in new array
        sorted[i] = array[ind];

        // update original array
        array[ind] = allmax;
    }

    // display sorted numbers
    printf("Sorted Numbers: \n===================\n");
    printArray(sorted, input_len);
    printSpace(2);

    return 0;
}
