#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>

using namespace std;

void usage()
{
  cout << "./getWorkTime [start_time] [end_time] <wasted_time>" << endl;
  cout << "'start_time' and 'end_time' are clock times, using decimals to represent minutes." << endl;
  cout << "'wasted_time' is the total amount of non-work time." << endl;
}

float getTotalTime(float start_time, float end_time)
{
  // declare variable
  float total_time;

  // deal with noon and afternoon times
  if (start_time == end_time || start_time > end_time)
    end_time = end_time + 12;

  // total time is the difference
  return total_time = end_time - start_time;
}

// -------------------------------

int main(int argc, char *argv[])
{
  // declare variables
  int num_inputs = argc - 1;
  float total_time;

  // function depending on inputs
  if (num_inputs < 2 || num_inputs > 3) {
    usage();
    return 1;
  }

  // if all inputs are provided correctly
  float start_time = atof(argv[1]);
  float end_time = atof(argv[2]);
  total_time = getTotalTime(start_time, end_time);

  // make sure getTotalTime did not return an error
  if (total_time == -1)
    return 1;

  // if there is a third input, subtract wasted time
  float wasted_time = 0;
  if (num_inputs == 3) {
    wasted_time = atof(argv[3]);
  }

  // display final work time
  cout << "Final work time: " << total_time - wasted_time << endl; 

  
  return 0;
}
