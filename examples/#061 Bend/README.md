# #061 Bend

Canonical entry from the corpus's `reference/languages.yml`. The reference and its order remain unchanged. The source was written for this example.

## Goal

Print Hello, World! through IO.print in the dialect Bend 2.

The original Bend 2 compiler is executed via Bun. The JavaScript backend produces the program then executed by Node; the compiler runtime effs must be available next to the output. This test covers Bend 2, not the previous HVM runtime.

## Toolchain and reproduction

Bend 2.0.36; Bun 1.4.2; Node.js 22.20.0

Command from the example folder, with the toolchain indicated available in the PATH. Run the build in a temporary copy to keep the generated files out of the corpus.

```text
bend hello.bend --check-only
bend hello.bend -o hello.js
```

```text
node hello.js
```

## Expected result and status

stdout esatto: Hello, World! seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records actual commands, versioni/provenienza of the toolchain, output codes, stdout/stderr and SHA-256 of the proven sources.

## Primary sources

- https://github.com/bendlang/bend
- https://github.com/bendlang/bend/blob/main/guide/GUIDE.md

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bend` | [hello.bend](hello.bend) verified |
