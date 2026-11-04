# #784 XCompose

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Analyze XCompose and produce Hello, World! from the Multi_key,h,w sequence.

The native XCompose parser reads a buffer fixture and the state machine receives three keysyms. No X server, physical keyboard or system configuration file is changed.

## Toolchain and reproduction

Libxkbcommon originale1.6.0, Python ctypes

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
python3 verify.py /path/to/libxkbcommon.so.0
```

## Expected result and status

State COMPOSED and string UTF8 Hello, World!.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://xkbcommon.org/doc/current/group__compose.html
