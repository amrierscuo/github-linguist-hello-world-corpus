# #698 TLA

Voce canonica `TLA`, tipo `programming`, language_id `364`.

Check a TLA model + finished with initial greeting and exact unchanged.

## Toolchain and reproduction

Original TLA + SANY parser and TLC finite-state model checker, TLA + tools release 1.8.0. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

TLA+ tools1.8.0 ufficiali, SANY e TLC.

Comando/procedura from the directory of the example, unless explicit indications:

```text
java -cp /path/to/tla2tools.jar tla2sany.SANY Hello.tla; java -cp /path/to/tla2tools.jar tlc2.TLC -cleanup -metadir build/states -config Hello.cfg Hello.tla
```

Expected result: Hello, World! in the conformed result, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

SANY accepts the module; TLC PrintT print of the value and completes the model checking with 1 state distinct and invariant without violations.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://lamport.azurewebsites.net/tla/tools.html](https://lamport.azurewebsites.net/tla/tools.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.tla` | [Hello.tla](Hello.tla) verified |
