cmake_minimum_required (VERSION 3.5)
project(playground)

# fetch all the local directories for generated code
get_filename_component(PROJECT_MODULES_DIR ./cmake/Modules ABSOLUTE)


########################################################
# Find Eigen
########################################################
find_package(Eigen3 QUIET)

if (NOT Eigen3_FOUND)
  include(LibFindMacros)
  libfind_pkg_check_modules(EIGEN_PKGCONFIG eigen3)
  if (EIGEN_PKGCONFIG_INCLUDE_DIRS STREQUAL "")
    message(FATAL_ERROR "could not find eigen either through find_package or pkgconfig")
  endif()
  set(EIGEN3_INCLUDE_DIR ${EIGEN_PKGCONFIG_INCLUDE_DIRS})
  message("Found Eigen with pkg-config, EIGEN3_INCLUDE_DIR: ${EIGEN3_INCLUDE_DIR}")
endif()


# # display webcam
# find_package(OpenCV REQUIRED)
# add_executable(displayWebcam src/displayWebcam.cpp)
# target_link_libraries(displayWebcam ${OpenCV_LIBS})

# # define library addition
# set(helper_fun_SRCS helper_functions.cpp)

# # add library
# add_library(helper_functions SHARED ${helper_fun_SRCS})
