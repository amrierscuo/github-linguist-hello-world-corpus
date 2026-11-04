# #624 Roff Manpage

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Render a man page describing the Hello, World! greeting.

The man page is distinct from the generic Roff; it uses TH, SH and PP. The ASCII rendering can contain overstrike sequences for titles and bold.

## Toolchain and reproduction

GNU groff1.23.0 e macro man

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
groff -Tascii -man hello.1
```

## Expected result and status

The DESCRIPTION section contains Hello, World!.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.gnu.org/software/groff/manual/groff.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.1` | [hello.1](hello.1) verified |
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
| `.man` | [hello.man](variants/man-ced7911e/hello.man) created; verification pending |
| `.mdoc` | [hello.mdoc](variants/mdoc-e2a9af6c/hello.mdoc) created; verification pending |
