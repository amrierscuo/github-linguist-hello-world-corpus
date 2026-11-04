# #781 X PixMap

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Read a raster XPM which visually shows Hello, World!.

The greeting string is designed in pixels, not in a comment. Pillow decoded the file82× 9; the assistant then inspected the original preview enlarged with nearest-neighbor and Hello, World! bed.

## Toolchain and reproduction

Pillow12.3.0 decoder XPM originale

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

Picture with Hello, World! black glyphs on white background; preview only in temporary build.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.x.org/docs/XPM/xpm.pdf

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.xpm` | [hello.xpm](hello.xpm) verified |
| `.pm` | [hello.pm](variants/pm-c810ce30/hello.pm) created; verification pending |
