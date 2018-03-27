#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, glob, shutil
from conans import ConanFile, AutoToolsBuildEnvironment, tools


class LKSCTPToolsConan(ConanFile):
    name = "lksctp-tools"
    version = "1.0.17"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False], "with_sctp": [True, False]}
    default_options = ("shared=False", "fPIC=True", "with_sctp=False")
    homepage = "http://lksctp.sourceforge.net/"
    url = "https://github.com/bincrafters/conan-lksctp-tools"
    description = "The lksctp-tools project provides a Linux user space library for SCTP"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "GPL-2.0, LGPL-2.1"
    exports = ["LICENSE.md"]
    source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/sctp/lksctp-tools"
        tools.get("{0}/archive/{1}-{2}.tar.gz".format(source_url, self.name, self.version))
        extracted_dir = self.name + "-" + self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def configure(self):
        if self.settings.os != "Linux":
            raise Exception("Linux Kernel SCTP Tools is only supported for Linux.")
        del self.settings.compiler.libcxx

    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        env_build.fpic = self.options.fPIC
        with tools.environment_append(env_build.vars):
            with tools.chdir(self.source_subfolder):
                self.run("./bootstrap")

            config_args = []
            config_args.append('--disable-%s' % ('static' if self.options.shared else 'shared'))
            config_args.append("--prefix=%s" % self.package_folder)
            config_args.append("--disable-tests")

            env_build.configure(configure_dir=self.source_subfolder, args=config_args)
            env_build.make()
            env_build.make(args=["install"])

    def package(self):
        self.copy(pattern="COPYING*", dst="licenses", src=self.source_subfolder, ignore_case=True, keep_path=False)
        self.move_withsctp()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.libs.append("dl")

    def move_withsctp(self):
        with tools.chdir(os.path.join(self.package_folder, "lib")):
            if not self.options.with_sctp:
                shutil.rmtree("lksctp-tools")
            else:
                with tools.chdir("lksctp-tools"):
                    for libfile in glob.glob("libwithsctp*"):
                        os.rename(libfile, os.path.join("..", libfile))
                os.rmdir("lksctp-tools")
