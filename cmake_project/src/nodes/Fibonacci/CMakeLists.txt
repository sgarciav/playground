##############################################
#          Library Creation                  #
##############################################
SET (LIBRARY_NAME Fibonacci_node)
SET (LIB_MAJOR 0)
SET (LIB_MINOR 0)
SET (LIB_RELEASE 1)

file(GLOB SRCS *.cpp)

add_executable(${LIBRARY_NAME} ${SRCS})

target_link_libraries(${LIBRARY_NAME}
  playground-core
  )

# if (OpenCV_FOUND)
#   target_link_libraries(${LIBRARY_NAME}
#     ${OpenCV_LIBRARIES}
#     scrimmage-opencv
#     )
# endif()

SET (_soversion ${LIB_MAJOR}.${LIB_MINOR}.${LIB_RELEASE})

set_target_properties(${LIBRARY_NAME}
  PROPERTIES
  SOVERSION ${LIB_MAJOR}
  VERSION ${_soversion}
  # LIBRARY_OUTPUT_DIRECTORY ${PROJECT_PLUGIN_LIBS_DIR}
  )

install(TARGETS ${LIBRARY_NAME}
  # IMPORTANT: Add the library to the "export-set"
  EXPORT ${PROJECT_NAME}-targets
  RUNTIME DESTINATION bin
  LIBRARY DESTINATION lib/${PROJECT_NAME}/node_libs
  )
