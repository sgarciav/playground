#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include "../helper_functions/helper_functions.h"

// print n spaces
void printSpace (int n)
{
     for (int i=1; i<=n; i++)
	  printf("\n");
}

// get minimum value from array
int getMinVal (int* v, int n)
{
     // placeholder
     int min_val = v[0];

     // go through all values
     for (int i=1; i<n; i++)
     {
	  if (v[i] < min_val)
	       min_val = v[i];
     }

     // return minimum value
     return min_val;
}

// get index of minimum value from array
int getMinInd (int* v, int n)
{
     // placeholder
     int min_ind = 0;
     int min_val = v[0];

     // go through all values
     for (int i=1; i<n; i++)
     {
	  if (v[i] < min_val)
	  {
	       min_val = v[i];
	       min_ind = i;
	  }
     }

     // return index of minimum value
     return min_ind;
}

// print array
void printArray (int* v, int n)
{
     for (int i=0; i<n; i++)
	  printf("%d ", v[i]);
     printSpace(1);
}
