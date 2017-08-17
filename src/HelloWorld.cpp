#include<math.h>
#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<iostream>
#include<vector>

using std::cout;
using std::endl;
using std::vector;

int main(int argc, char *argv[])
{
     printf("%s\n", "Hello World");

     for (int i=0; i < 15; i++) {
	  if (i == 10)
	       break;

	  printf("%d) do me \n", i);
     }

     printf("\n out! \n");
     
     // compare stirngs
     std::string str1 = "sergio";
     std::string str2 = "licia";
     std::string str3 = "sergio";
     std::string concat = str1 + str2;
     
     bool one_str = str1.compare(str2);
     bool two_str = str1.compare(str3);
     cout << "different: " << one_str << endl;
     cout << "same: " << two_str << endl;
     cout << concat << endl;

     // play with vectors
     vector<double> vec1;
     for (int i = 0; i < 10; i++) {
	  vec1.push_back(i);
     }
     for (int i = 0; i < vec1.size(); i++) {
	  cout << vec1[i] << endl;
     }

     // test input handling
     if (argc > 1) {
	  std::string input = argv[1];
	  cout << "input: " << input << endl;
	  cout << "number of inputs: " << argc << endl;
	  if (argc == 3) {
	       cout << "ERROR: Need as input the robot name." << endl;
	       exit(EXIT_FAILURE);
	  }
     }

     // test absolute value
     float one, two, three;
     one = -1.434;
     two = 2.434;
     three = -325.8745;
     cout << fabs(one) << ", " << fabs(two) << ", " << fabs(three) << endl;
     

     return 0;
}
