cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(libheif 1.5.1 REQUIRED CONFIG)

add_executable(example example.cpp)
target_link_libraries(example PRIVATE libheif)
