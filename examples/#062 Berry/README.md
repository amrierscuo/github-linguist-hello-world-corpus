# #062 Berry

Canonical entry from the corpus's `reference/languages.yml`. The reference and its order remain unchanged. The source was written for this example.

## Goal

Fill and execute a concatenation of strings in the VM Berry.

The build of the original interpreter only omits the optional readline dependence for the interactive console.The parser and VM of file execution are those of the upstream project.

## Toolchain and reproduction

Berry 1.1.0, original sources berry-lang/berry; GNU C on Ubuntu WSL

Command from the example folder, with the toolchain indicated available in the PATH. Run the build in a temporary copy to keep the generated files out of the corpus.

```text
make CFLAGS="-Wall -Wextra -std=c99 -O2" LIBS="-lm -ldl"
```

```text
berry hello.be
```

## Expected result and status

stdout esatto: Hello, World! seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records actual commands, versioni/provenienza of the toolchain, output codes, stdout/stderr and SHA-256 of the proven sources.

## Primary sources

- https://github.com/berry-lang/berry
- https://berry.readthedocs.io/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.be` | [hello.be](hello.be) verified |
