# #624 Roff Manpage

## Latest recorded verification

Latest extension checks:
- `.1in`: Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Evidence](verification/native_20261105_batch_2e31696e.json).
- `.1m`: Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Evidence](verification/native_20261105_batch_2e316d.json).
- `.1x`: Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Evidence](verification/native_20261105_batch_2e3178.json).
- `.2`: Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Evidence](verification/native_20261105_batch_2e32.json).
- `.3`: Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Evidence](verification/native_20261105_batch_2e33.json).
- `.3in`: Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Evidence](verification/native_20261105_batch_2e33696e.json).
- `.3m`: Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Evidence](verification/native_20261105_batch_2e336d.json).
- `.3p`: Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Evidence](verification/native_20261105_batch_2e3370.json).
- `.3pm`: Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Evidence](verification/native_20261105_batch_2e33706d.json).
- `.3qt`: Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Evidence](verification/native_20261105_batch_2e337174.json).
- `.3x`: Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Evidence](verification/native_20261105_batch_2e3378.json).
- `.4`: Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Evidence](verification/native_20261105_batch_2e34.json).
- `.5`: Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Evidence](verification/native_20261105_batch_2e35.json).
- `.6`: Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Evidence](verification/native_20261105_batch_2e36.json).
- `.7`: Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Evidence](verification/native_20261105_batch_2e37.json).
- `.8`: Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Evidence](verification/native_20261105_batch_2e38.json).
- `.9`: Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Evidence](verification/native_20261105_batch_2e39.json).
- `.man`: Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Evidence](verification/native_20261105_batch_2e6d616e.json).
- `.mdoc`: Native groff rendered the exact variant using its plain, man, mdoc, me or ms input as recorded; the rendered text contains Hello, World!. Macro includes were loaded natively when present. No GUI renderer was used. [Evidence](verification/native_20261105_batch_2e6d646f63.json).

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
| `.1in` | [hello.1in](variants/1in-6e7b1a94/hello.1in) syntax and behavior verified |
| `.1m` | [hello.1m](variants/1m-7f066f37/hello.1m) syntax and behavior verified |
| `.1x` | [hello.1x](variants/1x-7bfba87c/hello.1x) syntax and behavior verified |
| `.2` | [hello.2](variants/2-4d02623e/hello.2) syntax and behavior verified |
| `.3` | [hello.3](variants/3-935a3a42/hello.3) syntax and behavior verified |
| `.3in` | [hello.3in](variants/3in-5e94d8c2/hello.3in) syntax and behavior verified |
| `.3m` | [hello.3m](variants/3m-9b77779e/hello.3m) syntax and behavior verified |
| `.3p` | [hello.3p](variants/3p-3cf4f404/hello.3p) syntax and behavior verified |
| `.3pm` | [hello.3pm](variants/3pm-8f3210f6/hello.3pm) syntax and behavior verified |
| `.3qt` | [hello.3qt](variants/3qt-f5ff2f97/hello.3qt) syntax and behavior verified |
| `.3x` | [hello.3x](variants/3x-a9b9c037/hello.3x) syntax and behavior verified |
| `.4` | [hello.4](variants/4-33df2dbc/hello.4) syntax and behavior verified |
| `.5` | [hello.5](variants/5-4b1e53e6/hello.5) syntax and behavior verified |
| `.6` | [hello.6](variants/6-ae3ae580/hello.6) syntax and behavior verified |
| `.7` | [hello.7](variants/7-11de1834/hello.7) syntax and behavior verified |
| `.8` | [hello.8](variants/8-5429ab03/hello.8) syntax and behavior verified |
| `.9` | [hello.9](variants/9-523c2e7c/hello.9) syntax and behavior verified |
| `.man` | [hello.man](variants/man-ced7911e/hello.man) syntax and behavior verified |
| `.mdoc` | [hello.mdoc](variants/mdoc-e2a9af6c/hello.mdoc) syntax and behavior verified |