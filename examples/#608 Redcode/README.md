# #608 Redcode

Voce canonica `Redcode`, tipo `programming`, language_id `321`.

Upload an original Redcode warrior with ASCII greeting codes in its data segment.

## Toolchain and reproduction

Required genuine pmars compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

It requires pMARS ICWS - 94 with CORESIZE 8000 and access to the memory view of the simulator.

Comando/procedura from the directory of the example, unless explicit indications:

```text
pmars -a hello.cw; pmars hello.cw hello.cw
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Redcode does not possess I/O string: the goal is to assemble and observe the 13 operand A of the DAT, which reconstruct Hello, World!, while JMP maintains the process. Parser/simulatore missing; no claim to output console.

Remaining requirements:

- Required pmars compiler/runtime and matching host resources are not available/configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [http://www.koth.org/pmars/](http://www.koth.org/pmars/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cw` | [hello.cw](hello.cw) created; verification pending |
