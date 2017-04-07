"""Recipe validation for lksctp-tools-1.0.17
"""
from os import getenv
from conans import ConanFile, CMake


class TestLKSCTPToolsConan(ConanFile):
    """Build test using target package and execute all tests
    """
    target = "lksctp-tools"
    name = "%s-test" % target
    version = "1.0.17"
    author = "Uilian Ries <uilianries@gmail.com>"
    license = "GPL-2"
    settings = "os", "compiler", "build_type", "arch"
    channel = getenv("CONAN_CHANNEL", "testing")
    user = getenv("CONAN_USERNAME", "uilianries")
    requires = "%s/%s@%s/%s" % (target, version, user, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        cmake.configure(
            self, source_dir=self.conanfile_directory, build_dir="./")
        cmake.build(self)

    def imports(self):
        self.copy(pattern="*.so*", dst="bin", src="lib")

    def test(self):
        cmake = CMake(self.settings)
        cmake.configure(
            self, source_dir=self.conanfile_directory, build_dir="./")
        cmake.build(self, target="test")
