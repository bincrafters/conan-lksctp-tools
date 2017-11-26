"""Conan recipe for LKSCTP Tools
"""
import os
from tempfile import mkdtemp
from conans import ConanFile, AutoToolsBuildEnvironment, tools


class LKSCTPToolsConan(ConanFile):
    """Download LKSCTP Tools, build and create package
    """
    name = "lksctp-tools"
    version = "1.0.17"
    generators = "cmake", "txt"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    url = "https://github.com/uilianries/conan-lksctp-tools"
    description = "The lksctp-tools project provides a Linux user space library for SCTP"
    author = "Uilian Ries <uilianries@gmail.com>"
    license = "GPL-2"
    install_dir = mkdtemp(suffix=name)

    def source(self):
        source_url = "https://github.com/sctp/lksctp-tools"
        tools.get("{0}/archive/{1}-{2}.tar.gz".format(source_url, self.name, self.version))
        extracted_dir = self.name + "-" + self.name + "-" + self.version
        os.rename(extracted_dir, "sources")

    def configure(self):
        del self.settings.compiler.libcxx

    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        env_build.fpic = True
        with tools.environment_append(env_build.vars):
            with tools.chdir("sources"):
                self.run("./bootstrap")
                library_type = "--disable-static" if self.options.shared else "--disable-shared"
                self.run("./configure --prefix=%s --disable-tests %s" % (self.install_dir, library_type))
                self.run("make")
                self.run("make install")

    def package(self):
        self.copy(pattern="COPYING", dst=".", src="sources")
        self.copy(pattern="*.h", dst="include", src=os.path.join(self.install_dir, "include"))
        self.copy(pattern="*.a", dst="lib", src=os.path.join(self.install_dir, "lib"), keep_path=False)
        self.copy(pattern="*.so*", dst="lib", src=os.path.join(self.install_dir, "lib"), keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("dl")
