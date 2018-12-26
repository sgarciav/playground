SubDirList(SUBDIRS ${CMAKE_CURRENT_SOURCE_DIR})

# in case you need to remove a dir from the list
# list(REMOVE_ITEM SUBDIRS ReadArrowKeys)

FOREACH(subdir ${SUBDIRS})
  add_subdirectory(${subdir})
ENDFOREACH()

# set(PROJECT_PLUGINS ${PROJECT_PLUGINS} PARENT_SCOPE) # not sure if we need this
