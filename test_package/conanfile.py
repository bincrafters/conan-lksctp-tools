import os
from conans import ConanFile, CMake, tools, RunEnvironment


class LksctpTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir=self.conanfile_directory, build_dir=os.getcwd())
        cmake.build()

    def test(self):
        with tools.environment_append(RunEnvironment(self).vars):
            if self.settings.os == "Windows":
                self.run(os.path.join("bin","test_package"))
            else:
                self.run("DYLD_LIBRARY_PATH=%s %s"%(os.environ['DYLD_LIBRARY_PATH'],os.path.join("bin","test_package")))
