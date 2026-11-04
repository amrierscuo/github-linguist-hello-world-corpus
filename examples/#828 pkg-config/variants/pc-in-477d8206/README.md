# 0828: pkg-config: `.pc.in`

Pkg-config template with real Autoconf placeholder; it requires replacement before use.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.pc.in`.

Control provided, from the folder of the variant:

```text
configure/CMake configure_file: replace @prefix@ with /corpus/example and @PACKAGE_VERSION@ with 1.0.0; write /absolute/work/pkg-config/hello.pc
PKG_CONFIG_PATH=/absolute/work/pkg-config pkg-config --variable=greeting hello
```

Expected result: variable greeting = Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://people.freedesktop.org/~dbn/pkg-config-guide.html](https://people.freedesktop.org/~dbn/pkg-config-guide.html)
