##############################################
#          Library Creation                  #
##############################################
SET (LIBRARY_NAME playground-core)
SET (LIB_MAJOR 0)
SET (LIB_MINOR 0)
SET (LIB_RELEASE 1)

set(SRCS
  common/helper_functions.cpp
  )

add_library(${LIBRARY_NAME} SHARED
  ${SRCS}
  )

# add_dependencies(${LIBRARY_NAME}
#   # dependencies
# )

SET (_soversion ${LIB_MAJOR}.${LIB_MINOR}.${LIB_RELEASE})

# target_link_libraries(${LIBRARY_NAME}
#   # libraries
# )

set_target_properties(
  ${LIBRARY_NAME}
  PROPERTIES
  SOVERSION ${LIB_MAJOR}
  VERSION ${_soversion}
  )

target_include_directories(${LIBRARY_NAME}
  PUBLIC
  "$<BUILD_INTERFACE:${PLAYGROUND_INC_DIR}>"
  )

install(TARGETS ${LIBRARY_NAME}
  # IMPORTANT: Add the library to the "export-set"
  EXPORT ${PROJECT_NAME}-targets
  RUNTIME DESTINATION bin
  LIBRARY DESTINATION lib
  )

##############################################
# Recurse into nodes
##############################################
add_subdirectory(nodes)
