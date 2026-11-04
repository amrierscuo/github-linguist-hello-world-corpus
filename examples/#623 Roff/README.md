# #623 Roff

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Render the Hello, World! paragraph in Roff.

Original roff document without macro package; the test uses formatter and postprocessor GNU groff.

## Toolchain and reproduction

GNU groff1.23.0

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
groff -Tascii hello.roff
```

## Expected result and status

Text output contains Hello, World!.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.gnu.org/software/groff/manual/groff.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.roff` | [hello.roff](hello.roff), [main.roff](variants/tmac-730eca82/main.roff) created; verification pending |
| `.1` | [hello.1](variants/1-f7f4791a/hello.1) created; verification pending |
| `.1in` | [hello.1in](variants/1in-6e7b1a94/hello.1in) created; verification pending |
| `.1m` | [hello.1m](variants/1m-7f066f37/hello.1m) created; verification pending |
| `.1x` | [hello.1x](variants/1x-7bfba87c/hello.1x) created; verification pending |
| `.2` | [hello.2](variants/2-4d02623e/hello.2) created; verification pending |
| `.3` | [hello.3](variants/3-935a3a42/hello.3) created; verification pending |
| `.3in` | [hello.3in](variants/3in-5e94d8c2/hello.3in) created; verification pending |
| `.3m` | [hello.3m](variants/3m-9b77779e/hello.3m) created; verification pending |
| `.3p` | [hello.3p](variants/3p-3cf4f404/hello.3p) created; verification pending |
| `.3pm` | [hello.3pm](variants/3pm-8f3210f6/hello.3pm) created; verification pending |
| `.3qt` | [hello.3qt](variants/3qt-f5ff2f97/hello.3qt) created; verification pending |
| `.3x` | [hello.3x](variants/3x-a9b9c037/hello.3x) created; verification pending |
| `.4` | [hello.4](variants/4-33df2dbc/hello.4) created; verification pending |
| `.5` | [hello.5](variants/5-4b1e53e6/hello.5) created; verification pending |
| `.6` | [hello.6](variants/6-ae3ae580/hello.6) created; verification pending |
| `.7` | [hello.7](variants/7-11de1834/hello.7) created; verification pending |
| `.8` | [hello.8](variants/8-5429ab03/hello.8) created; verification pending |
| `.9` | [hello.9](variants/9-523c2e7c/hello.9) created; verification pending |
| `.l` | [hello.l](variants/l-ac16c41b/hello.l) created; verification pending |
| `.man` | [hello.man](variants/man-ced7911e/hello.man) created; verification pending |
| `.mdoc` | [hello.mdoc](variants/mdoc-e2a9af6c/hello.mdoc) created; verification pending |
| `.me` | [hello.me](variants/me-a72dc235/hello.me) created; verification pending |
| `.ms` | [hello.ms](variants/ms-5138d9ae/hello.ms) created; verification pending |
| `.n` | [hello.n](variants/n-3852639b/hello.n) created; verification pending |
| `.nr` | [hello.nr](variants/nr-ec75feb3/hello.nr) created; verification pending |
| `.rno` | [hello.rno](variants/rno-4ebd8568/hello.rno) created; verification pending |
| `.tmac` | [hello.tmac](variants/tmac-730eca82/hello.tmac) created; verification pending |
