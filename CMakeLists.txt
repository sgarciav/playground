# Specify the minimum version for CMake
cmake_minimum_required(VERSION 2.8)

# display webcam
find_package(OpenCV REQUIRED)
add_executable(displayWebcam src/displayWebcam.cpp)
target_link_libraries(displayWebcam ${OpenCV_LIBS})

# # define library addition
# set(helper_fun_SRCS helper_functions.cpp)

# # add library
# add_library(helper_functions SHARED ${helper_fun_SRCS})
