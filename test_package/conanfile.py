from conans import ConanFile, CMake, tools, RunEnvironment
import os


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        argument = "with_sctp" if self.options['lksctp-tools'].with_sctp else ""
        with tools.environment_append(RunEnvironment(self).vars):
            bin_path = os.path.join("bin", "test_package")
            self.run("LD_LIBRARY_PATH=%s %s %s" % (os.environ.get('LD_LIBRARY_PATH', ''), bin_path, argument))
