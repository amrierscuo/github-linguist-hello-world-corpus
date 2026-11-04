# #074 Bluespec BH

Canonical entry from the corpus's `reference/languages.yml`. The reference and its order remain unchanged. The source was written for this example.

## Goal

Simulate a rule in the Bluespec Haskell dialect that prints Hello, World! and ends.

Hello.bs is in the BH dialect: Module, rules, when and action, with significant indentation. The BSC compiler accepts this dialect and generates the Bluesim simulator; it is not a copy of a BSV file with other extension.

## Toolchain and reproduction

B-Lang BSC 2026.07.1 for Ubuntu 24.04; GNU C++; Tcl 8.6.14 isolated

Command from the example folder, with the toolchain indicated available in the PATH. Run the build in a temporary copy to keep the generated files out of the corpus.

```text
bsc -u -sim -g mkHello Hello.bs
bsc -sim -e mkHello -o hello
```

```text
./hello
```

## Expected result and status

stdout esatto Hello, World! seguito da newline; simulazione exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records actual commands, versioni/provenienza of the toolchain, output codes, stdout/stderr and SHA-256 of the proven sources.

## Primary sources

- https://bluespec.dev/bh-reference/expressions-modules.html
- https://bluespec.dev/bh-reference/expressions-rules.html
- https://github.com/B-Lang-org/bsc/releases/tag/2026.07.1

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bs` | [Hello.bs](Hello.bs) verified |
