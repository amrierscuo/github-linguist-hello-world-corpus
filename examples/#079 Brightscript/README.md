# #079 Brightscript

Canonical entry from the corpus's `reference/languages.yml`. The reference and its order remain unchanged. The source was written for this example.

## Goal

Perform sub main and print Hello, World! in BrightScript language.

The Linguist canonical entry is Brightscript. The code uses the Roku BrightScript language; the actual test takes place through brs in Node, without hardware or API of a Roku device.

## Toolchain and reproduction

brs 0.45.0, interpreter BrightScript of the original community; Node.js 22.20.0

Command from the example folder, with the toolchain indicated available in the PATH. Run the build in a temporary copy to keep the generated files out of the corpus.

```text
brs hello.brs
```

## Expected result and status

stdout esatto Hello, World! seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records actual commands, versioni/provenienza of the toolchain, output codes, stdout/stderr and SHA-256 of the proven sources.

## Primary sources

- https://github.com/sjbarag/brs
- https://developer.roku.com/docs/references/brightscript/language/expressions-variables-types.md

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.brs` | [hello.brs](hello.brs) verified |
