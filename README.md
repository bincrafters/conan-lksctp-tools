[![Build Status](https://travis-ci.org/uilianries/conan-lksctp-tools.svg?branch=release/1.0.17)](https://travis-ci.org/uilianries/conan-lksctp-tools) [![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://img.shields.io/badge/License-GPL%20v2-blue.svg)

# Linux Kernel Stream Control Transmission Protocol Tools

[Conan.io](https://conan.io) package for [lksctp-tools](https://github.com/sctp/lksctp-tools) project

The packages generated with this **conanfile** can be found in [conan.io](https://conan.io/source/lksctp-tools/1.0.17/uilianries/stable).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

If your are in Windows you should run it from a VisualStudio console in order to get "mc.exe" in path.
    
## Upload packages to server

    $ conan upload lksctp-tools/1.0.17@uilianries/stable --all
    
## Reuse the packages

### Basic setup

    $ conan install lksctp-tools/1.0.17@uilianries/stable
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    lksctp-tools/1.0.17@uilianries/stable

    [options]
    lksctp-tools:shared=True # False
    
    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

### License
[GPL-2](LICENSE)
