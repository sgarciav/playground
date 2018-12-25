##############################################
#          Library Creation                  #
##############################################
SET (LIBRARY_NAME DisplayWebcam_node)
SET (LIB_MAJOR 0)
SET (LIB_MINOR 0)
SET (LIB_RELEASE 1)

file(GLOB SRCS *.cpp)

if(NOT TARGET playground-opencv)
  message(WARNING "Not building DisplayWebcom node. Depends on OpenCV.")
  return()
endif()

add_executable(${LIBRARY_NAME} ${SRCS})

target_link_libraries(${LIBRARY_NAME}
  playground-core
  playground-opencv
  )

SET (_soversion ${LIB_MAJOR}.${LIB_MINOR}.${LIB_RELEASE})

set_target_properties(${LIBRARY_NAME}
  PROPERTIES
  SOVERSION ${LIB_MAJOR}
  VERSION ${_soversion}
  )

install(TARGETS ${LIBRARY_NAME}
  # IMPORTANT: Add the library to the "export-set"
  EXPORT ${PROJECT_NAME}-targets
  RUNTIME DESTINATION bin
  LIBRARY DESTINATION lib/${PROJECT_NAME}/node_libs
  )
