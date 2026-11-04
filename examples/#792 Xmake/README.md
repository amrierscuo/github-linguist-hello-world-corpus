# #792 Xmake

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Play xmake.lua, fill in the fixture C and execute Hello, World!.

Xmake interprets target, set_kind and add_files and invokes GCC. Cache/configurazione and build of the test are isolated in work.

## Toolchain and reproduction

Xmake3.1.1+HEAD.3ba37a0 bundle originale e GCC Ubuntu

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
xmake f -y -p linux --toolchain=gcc -o build; xmake -y; ./build/linux/x86_64/release/hello
```

## Expected result and status

Build exit0 and compiled Hello, World! print program.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://xmake.io/guide/quick-start.html
