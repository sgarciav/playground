#include <Eigen/Dense>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <memory>

using std::cout;
using std::endl;
using std::vector;

template <typename T>
void print_matrix(T A) {
    cout << "eigen matrix: " << endl;
    cout << A << endl;
}

int main(int argc, char *argv[]) {

    printf("%s\n", "Hello World");

    for (int i = 0; i < 15; i++) {
        if (i == 10) {
            break;
        }

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

    // test Eigen vector
    // To compile: g++ -o HelloWorld ../src/HelloWorld.cpp -std=c++11 -I/usr/include/eigen3
    Eigen::Vector3d p;
    p << 1,
        2,
        3;
    cout << "eigen vector: " << endl;
    cout << p << " | magnitude: " << p.norm() << endl;

    p.normalize();
    cout << "eigen vector normalized: " << endl;
    cout << p << " | magnitude: " << p.norm() << endl;

    Eigen::MatrixXd P;
    P.resize(3,1);
    P << 1,
        4,
        7;
    const int a = 3;
    const int b = 1;
    print_matrix<Eigen::Matrix<double, a, b>>(P);

    // count character occurances in string
    std::string s = "the answer; should ;be ;; four";
    size_t n = std::count(s.begin(), s.end(), ';');
    cout << "; count " << n << endl;

    // map of multiple fields
    typedef std::tuple<double, int, double, std::string> rowtype;
    std::map<int, rowtype> big_map;

    int k = 0;
    for (const auto& kv : big_map) {
        cout << k++ << endl;
    }

    rowtype row1 = std::make_tuple(1.5, 2, 3.2, "sergio");
    rowtype row2 = std::make_tuple(5, 6, 7.7, "licia");

    big_map[1] = row1;
    big_map[2] = row2;

    cout << endl << "names:" << endl;
    for (const auto& kv : big_map) {
        cout << std::get<3>(kv.second) << endl;
    }

    rowtype row3 = std::make_tuple(5, 6, 7.7, "mami");

    cout << endl << "new names:" << endl;
    big_map[1] = row3;
    for (const auto& kv : big_map) {
        cout << std::get<3>(kv.second) << endl;
    }

    // if statements
    bool if1 = true;
    bool if2 = false;
    double printme = (if1) ? ((if2) ? 3 : 4) : 2;
    cout << " " << endl;
    cout << printme << endl;

    // shared pointers
    auto foo = std::make_shared<int>(10);
    cout << endl << "foo original: " << *foo << endl;
    *foo = *foo + 20;
    cout << "foo updated: " << *foo << endl;

    // return name of latest modified file in directory
    std::string cmd_result;
    std::string directory = "/home/sgarcia/Desktop";
    FILE * stream;
    const int max_buffer = 256;
    char buffer[max_buffer];
    std::string cmd = "ls -trp " + directory + " | grep -v / | tail -1";
    cmd.append(" 2>&1");

    stream = popen(cmd.c_str(), "r");
    if (stream) {
        while (!feof(stream))
            if (fgets(buffer, max_buffer, stream) != NULL) cmd_result.append(buffer);
        pclose(stream);
    }
    cout << " " << endl;
    cout << "command result: " << cmd_result << endl;

    return 0;
}
