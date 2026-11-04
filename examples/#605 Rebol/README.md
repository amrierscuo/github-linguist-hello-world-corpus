# #605 Rebol

## Latest recorded verification

Latest extension checks:
- `.r`: Rebol/Bulk original interpreter executes the exact variant filename as a console program. [Evidence](verification/native_20261104_followup_2e72.json).
- `.r2`: Rebol/Bulk original interpreter executes the exact variant filename as a console program. [Evidence](verification/native_20261104_followup_2e7232.json).
- `.r3`: Rebol/Bulk original interpreter executes the exact variant filename as a console program. [Evidence](verification/native_20261104_followup_2e7233.json).
- `.rebol`: Rebol/Bulk original interpreter executes the exact variant filename as a console program. [Evidence](verification/native_20261104_followup_2e7265626f6c.json).

Voce canonica `Rebol`, tipo `programming`, language_id `319`.

Run a Rebol program with rejoin and print.

## Toolchain and reproduction

Original Rebol3 Oldes branch interpreter — Rebol/Bulk 3.22.1 (2026-05-27 19:59:00 UTC); Copyright (c) 2012 REBOL Technologies; Copyright (c) 2012-2026 Rebol Open Source Contributors; Source:       https://github.com/Oldes/Rebol3. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Rebol/Bulk 3.22.1 Oldes branch, original Linux x64 release. SHA of the axit corresponds to the primary release.

Comando/procedura from the directory of the example, unless explicit indications:

```text
rebol3 -q hello.reb
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Genuine Interpreter, original script and exact stdout. The Windows track does not work in the non-interactive test terminal, so it used the official Linux runtime.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/Oldes/Rebol3](https://github.com/Oldes/Rebol3)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.reb` | [hello.reb](hello.reb) verified |
| `.r` | [hello.r](variants/r-8dbb84b2/hello.r) syntax and behavior verified |
| `.r2` | [hello.r2](variants/r2-8d1288b8/hello.r2) syntax and behavior verified |
| `.r3` | [hello.r3](variants/r3-172ccdf0/hello.r3) syntax and behavior verified |
| `.rebol` | [hello.rebol](variants/rebol-747e1472/hello.rebol) syntax and behavior verified |