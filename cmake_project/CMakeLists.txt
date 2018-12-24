cmake_minimum_required (VERSION 3.5)

# see : https://crascit.com/2016/04/09/using-ccache-with-cmake/
find_program(CCACHE_PROGRAM ccache)
if(CCACHE_PROGRAM)
  set_property(GLOBAL PROPERTY RULE_LAUNCH_COMPILE "${CCACHE_PROGRAM}")
else()
  message("ccache not found, repeated builds will be faster if this program is installed")
endif()

project(playground)

# fetch all the local directories for generated code
get_filename_component(PLAYGROUND_INC_DIR ./include ABSOLUTE)

# include cmake files
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${PROJECT_SOURCE_DIR}/cmake/Modules)

include(MacroSubDirList)

# Recurse into src
add_subdirectory(src)

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

if (Eigen3_FOUND)
  add_library(playground-eigen INTERFACE)
  target_include_directories(playground-eigen SYSTEM INTERFACE ${EIGEN3_INCLUDE_DIR})
  install(TARGETS playground-eigen EXPORT ${PROJECT_NAME}-targets)
  list(APPEND PROJECT_TARGETS playground-eigen)
else()
  message(WARNING "Eigen package not found. Install Eigen by executing: ") # TODO: how to install eigen
endif()


########################################################
# Find OpenCV
########################################################
find_package(OpenCV QUIET)
if (OpenCV_FOUND)
  add_library(playground-opencv INTERFACE)
  target_include_directories(playground-opencv SYSTEM INTERFACE ${OpenCV_INCLUDE_DIRS})
  # target_compile_definitions(playground-opencv INTERFACE -DENABLE_OPENCV=1)
  install(TARGETS playground-opencv EXPORT ${PROJECT_NAME}-targets)
  list(APPEND PROJECT_TARGETS playground-opencv)
else()
  messsage(WARNING "OpenCV package not found. Install OpenCV by executing:") # TODO: how to install opencv
endif()


#############################################################################
# Generate the cmake configuration files for the build tree
#############################################################################
list(LENGTH PROJECT_TARGETS NUM_TARGETS)
# include(CMakePackageConfigHelpers)

# configure_package_config_file(
#   ${PROJECT_SOURCE_DIR}/cmake/Modules/project-config.cmake.in
#   ${PROJECT_BINARY_DIR}/${PROJECT_NAME}-config.cmake
#   INSTALL_DESTINATION ${PROJECT_BINARY_DIR}
#   )

# Export project export set to the build tree
if(${NUM_TARGETS} GREATER 0)
  export(
    EXPORT ${PROJECT_NAME}-targets
    FILE "${PROJECT_BINARY_DIR}/${PROJECT_NAME}-targets.cmake"
    )
endif()

# Export the package for use from the build-tree
# (this registers the build-tree with a global CMake-registry ~/.cmake)
export(PACKAGE ${PROJECT_NAME})



# # display webcam
# find_package(OpenCV REQUIRED)
# add_executable(displayWebcam src/displayWebcam.cpp)
# target_link_libraries(displayWebcam ${OpenCV_LIBS})

# # define library addition
# set(helper_fun_SRCS helper_functions.cpp)

# # add library
# add_library(helper_functions SHARED ${helper_fun_SRCS})
