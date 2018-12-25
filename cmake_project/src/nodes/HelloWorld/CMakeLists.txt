##############################################
#          Library Creation                  #
##############################################
SET (LIBRARY_NAME HelloWorld_node)
SET (LIB_MAJOR 0)
SET (LIB_MINOR 0)
SET (LIB_RELEASE 1)

file(GLOB SRCS *.cpp)

if(NOT TARGET playground-eigen)
  message(WARNING "Not building HelloWorld node. Depends on Eigen.")
  return()
endif()

add_executable(${LIBRARY_NAME} ${SRCS})

target_link_libraries(${LIBRARY_NAME}
  playground-core
  playground-eigen
  )

SET (_soversion ${LIB_MAJOR}.${LIB_MINOR}.${LIB_RELEASE})

set_target_properties(${LIBRARY_NAME}
  PROPERTIES
  SOVERSION ${LIB_MAJOR}
  VERSION ${_soversion}
  )
