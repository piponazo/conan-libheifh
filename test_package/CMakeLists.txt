cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

find_package(libheif 1.5.1 REQUIRED CONFIG)

add_executable(example example.cpp)
target_link_libraries(example PRIVATE libheif)
