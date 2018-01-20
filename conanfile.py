import os
from conans import ConanFile, AutoToolsBuildEnvironment, tools


class LKSCTPToolsConan(ConanFile):
    name = "lksctp-tools"
    version = "1.0.17"
    generators = "cmake", "txt"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    url = "https://github.com/uilianries/conan-lksctp-tools"
    description = "The lksctp-tools project provides a Linux user space library for SCTP"
    author = "Uilian Ries <uilianries@gmail.com>"
    license = "GPL-2.0, LGPL-2.1"
    exports = ["LICENSE.md"]

    source_subfolder = "source_subfolder"
    install_subfolder = 'install_subfolder'

    def source(self):
        source_url = "https://github.com/sctp/lksctp-tools"
        tools.get("{0}/archive/{1}-{2}.tar.gz".format(source_url, self.name, self.version))
        extracted_dir = self.name + "-" + self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def configure(self):
        del self.settings.compiler.libcxx

    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        env_build.fpic = True
        with tools.environment_append(env_build.vars):
            with tools.chdir(self.source_subfolder):
                self.run("./bootstrap")
        
            config_args = []
            if self.options.shared:
                config_args.append('--disable-static')
            else:
                config_args.append('--disable-shared')
            prefix = os.path.abspath(self.install_subfolder)
            config_args.append("--prefix=%s" % prefix)
            config_args.append("--disable-tests")

            env_build.configure(configure_dir=self.source_subfolder, args=config_args)
            env_build.make()
            env_build.make(args=["install"])

    def package(self):
        self.copy(pattern="COPYING*", dst="licenses", src=self.source_subfolder, ignore_case=True, keep_path=False)
        self.copy(pattern="*.h", dst="include", src=os.path.join(self.install_subfolder, "include"))
        self.copy(pattern="*.a", dst="lib", src=os.path.join(self.install_subfolder, "lib"), keep_path=False)
        self.copy(pattern="*.so*", dst="lib", src=os.path.join(self.install_subfolder, "lib"), keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("dl")
