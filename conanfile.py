from conans import ConanFile, CMake, tools


class LibheifConan(ConanFile):
    name = "libheif"
    version = "1.5.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Libheif here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    def source(self):
        # TODO: Point to the upstream repo + use tarballs
        self.run("git clone https://github.com/piponazo/libheif.git --branch cmakeImprovements --depth 1")
        tools.replace_in_file("libheif/CMakeLists.txt", "cmake_policy(SET CMP0054 NEW)",
                              '''cmake_policy(SET CMP0054 NEW)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="libheif")
        cmake.build()
        cmake.install()

