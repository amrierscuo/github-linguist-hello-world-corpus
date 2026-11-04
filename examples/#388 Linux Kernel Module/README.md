# #388 Linux Kernel Module

Associate metadata .mod and Kbuild to the original form that contains the greeting.

## Toolchain

Linux kernel headers/toolchain Kbuild compatibili; versione da registrare

## Commands and procedure

Copy Kbuild/hello.c in build; make -C <kernel-headers> M=< path-absolute-build> modules; compare hello.mod by normalizing the prefix of the object folder

## Expected result

Kbuild generates hello.mod reported to hello.o; offline build accepted; module contains message and MODULE_DESCRIPTION of greeting.

## Status

Syntax and behavioral verification pending.

Linux Kernel Module in the baseline is a .mod. hello.mod data format is the textual sample of the object list, with its illustrative path; Kbuild and hello.c provide the real context. It is not a .ko binary and cannot be loaded directly. The future predicted verification is compilazione/metadata offline; init/runtime kernel is not certified

Remaining requirements:
- Header/build tree kbuild kernel not prepared; offline compilation and .mod pending regeneration.

## Primary sources

- [https://docs.kernel.org/kbuild/modules.html](https://docs.kernel.org/kbuild/modules.html)
- [https://docs.kernel.org/kbuild/makefiles.html](https://docs.kernel.org/kbuild/makefiles.html)
- [https://github.com/torvalds/linux/blob/master/scripts/Makefile.build](https://github.com/torvalds/linux/blob/master/scripts/Makefile.build)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mod` | [hello.mod](hello.mod) created; verification pending |
