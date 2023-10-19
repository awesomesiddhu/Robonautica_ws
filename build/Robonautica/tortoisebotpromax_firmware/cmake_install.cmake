# Install script for directory: /home/siddharth/catkin_workspace/src/Robonautica/tortoisebotpromax_firmware

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/siddharth/catkin_workspace/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tortoisebotpromax_firmware/msg" TYPE FILE FILES "/home/siddharth/catkin_workspace/src/Robonautica/tortoisebotpromax_firmware/msg/Diff.msg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tortoisebotpromax_firmware/cmake" TYPE FILE FILES "/home/siddharth/catkin_workspace/build/Robonautica/tortoisebotpromax_firmware/catkin_generated/installspace/tortoisebotpromax_firmware-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/siddharth/catkin_workspace/devel/include/tortoisebotpromax_firmware")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/siddharth/catkin_workspace/devel/share/roseus/ros/tortoisebotpromax_firmware")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/siddharth/catkin_workspace/devel/share/common-lisp/ros/tortoisebotpromax_firmware")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/siddharth/catkin_workspace/devel/share/gennodejs/ros/tortoisebotpromax_firmware")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/siddharth/catkin_workspace/devel/lib/python3/dist-packages/tortoisebotpromax_firmware")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/siddharth/catkin_workspace/devel/lib/python3/dist-packages/tortoisebotpromax_firmware")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/siddharth/catkin_workspace/build/Robonautica/tortoisebotpromax_firmware/catkin_generated/installspace/tortoisebotpromax_firmware.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tortoisebotpromax_firmware/cmake" TYPE FILE FILES "/home/siddharth/catkin_workspace/build/Robonautica/tortoisebotpromax_firmware/catkin_generated/installspace/tortoisebotpromax_firmware-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tortoisebotpromax_firmware/cmake" TYPE FILE FILES
    "/home/siddharth/catkin_workspace/build/Robonautica/tortoisebotpromax_firmware/catkin_generated/installspace/tortoisebotpromax_firmwareConfig.cmake"
    "/home/siddharth/catkin_workspace/build/Robonautica/tortoisebotpromax_firmware/catkin_generated/installspace/tortoisebotpromax_firmwareConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tortoisebotpromax_firmware" TYPE FILE FILES "/home/siddharth/catkin_workspace/src/Robonautica/tortoisebotpromax_firmware/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/siddharth/catkin_workspace/build/Robonautica/tortoisebotpromax_firmware/catkin_generated/installspace/tortoisebotpromax_firmware.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tortoisebotpromax_firmware/cmake" TYPE FILE FILES "/home/siddharth/catkin_workspace/build/Robonautica/tortoisebotpromax_firmware/catkin_generated/installspace/tortoisebotpromax_firmware-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tortoisebotpromax_firmware/cmake" TYPE FILE FILES
    "/home/siddharth/catkin_workspace/build/Robonautica/tortoisebotpromax_firmware/catkin_generated/installspace/tortoisebotpromax_firmwareConfig.cmake"
    "/home/siddharth/catkin_workspace/build/Robonautica/tortoisebotpromax_firmware/catkin_generated/installspace/tortoisebotpromax_firmwareConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tortoisebotpromax_firmware" TYPE FILE FILES "/home/siddharth/catkin_workspace/src/Robonautica/tortoisebotpromax_firmware/package.xml")
endif()

