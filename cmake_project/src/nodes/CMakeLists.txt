SubDirList(SUBDIRS ${CMAKE_CURRENT_SOURCE_DIR})

list(REMOVE_ITEM SUBDIRS DisplayWebcam) # in case you need to remove a dir from the list
list(REMOVE_ITEM SUBDIRS HelloWorld)
list(REMOVE_ITEM SUBDIRS NumberOfElements)
list(REMOVE_ITEM SUBDIRS ReadArrowKeys)
list(REMOVE_ITEM SUBDIRS SortNums)
list(REMOVE_ITEM SUBDIRS WorkTime)


FOREACH(subdir ${SUBDIRS})
  add_subdirectory(${subdir})
ENDFOREACH()

# set(PROJECT_PLUGINS ${PROJECT_PLUGINS} PARENT_SCOPE) # not sure if we need this
