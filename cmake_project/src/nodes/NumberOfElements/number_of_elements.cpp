#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int _a[] = {1, 2, 3, 4, 5};
vector<int> a(_a, _a+(sizeof(_a)/sizeof(_a[0])));

int main(int argc, char *argv[]) {

    // number of inouts
    int num_inputs = argc - 1;

    // incput vector
    float v_in[num_inputs];
    for (int i = 1; i <= num_inputs; i++) {
        v_in[i] = atof(argv[i]);
    }

    // change to vector notation
    vector<float> v(v_in, v_in+(sizeof(v_in)/sizeof(v_in[0])));

    // display all elements in array
    cout << "The inut array is: ";
    for (size_t i = 1; i <= v.size(); i++) {
        cout << v[i] << " ";
    }
    cout << endl;
    cout << "Count: " << v.size() << endl;


    return 0;
}
