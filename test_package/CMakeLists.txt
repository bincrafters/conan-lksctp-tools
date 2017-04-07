PROJECT(conan-lksctp-tools-test)
cmake_minimum_required(VERSION 2.8)

# Verbose mode #################################################################
set(CMAKE_VERBOSE_MAKEFILE 1)

# Conan package ################################################################
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Header files #################################################################
include_directories(include)

# Source files #################################################################
file(GLOB SOURCE_FILES src/*.c)

# Build applications ###########################################################
add_executable(${PROJECT_NAME} ${SOURCE_FILES})
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})

# Add test #####################################################################
enable_testing()
add_test(NAME test-all
         WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
         COMMAND ${PROJECT_NAME})
