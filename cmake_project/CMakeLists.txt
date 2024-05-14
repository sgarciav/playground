cmake_minimum_required (VERSION 3.5)

# see : https://crascit.com/2016/04/09/using-ccache-with-cmake/
find_program(CCACHE_PROGRAM ccache)
if(CCACHE_PROGRAM)
  set_property(GLOBAL PROPERTY RULE_LAUNCH_COMPILE "${CCACHE_PROGRAM}")
else()
  message("ccache not found, repeated builds will be faster if this program is installed")
endif()

project(playground)

add_compile_options(-std=c++11)

# fetch all the local directories for generated code
get_filename_component(PLAYGROUND_INC_DIR ./include ABSOLUTE)
get_filename_component(PROJECT_MODULES_DIR ./cmake/Modules ABSOLUTE)

# include cmake files
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${PROJECT_MODULES_DIR})

include(MacroSubDirList)

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
  add_library(${PROJECT_NAME}-eigen INTERFACE)
  target_include_directories(${PROJECT_NAME}-eigen SYSTEM INTERFACE ${EIGEN3_INCLUDE_DIR})
  install(TARGETS ${PROJECT_NAME}-eigen EXPORT ${PROJECT_NAME}-targets)
  list(APPEND PROJECT_TARGETS ${PROJECT_NAME}-eigen)
else()
  message(WARNING "Eigen package not found. Install the libeigen3-dev package")
endif()


########################################################
# Find OpenCV
########################################################
find_package(OpenCV QUIET)
if (OpenCV_FOUND)
  add_library(${PROJECT_NAME}-opencv INTERFACE)
  target_include_directories(${PROJECT_NAME}-opencv SYSTEM INTERFACE ${OpenCV_INCLUDE_DIRS})
  target_link_libraries(${PROJECT_NAME}-opencv INTERFACE ${OpenCV_LIBRARIES})
  install(TARGETS ${PROJECT_NAME}-opencv EXPORT ${PROJECT_NAME}-targets)
  list(APPEND PROJECT_TARGETS ${PROJECT_NAME}-opencv)
else()
  message(WARNING "OpenCV package not found. Install OpenCV by executing:") # TODO: how to install opencv
endif()


########################################################
# Find Curses (ncurses)
########################################################
set(CURSES_NEED_NCURSES True) # See: https://cmake.org/cmake/help/v3.0/module/FindCurses.html
find_package(Curses QUIET)
if (CURSES_FOUND)
  add_library(${PROJECT_NAME}-curses INTERFACE)
  target_include_directories(${PROJECT_NAME}-curses SYSTEM INTERFACE ${CURSES_INCLUDE_DIR})
  target_link_libraries(${PROJECT_NAME}-curses INTERFACE ${CURSES_LIBRARIES})
  install(TARGETS ${PROJECT_NAME}-curses EXPORT ${PROJECT_NAME}-targets)
  list(APPEND PROJECT_TARGETS ${PROJECT_NAME}-curses)
else()
  message(WARNING "Curses package not found. Install Curses by executing: sudo apt-get install libncurses5-dev")
endif()


#############################################################################
# Recurse into src
#############################################################################
add_subdirectory(src)


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
