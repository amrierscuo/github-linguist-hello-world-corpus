# #696 TI Program

Voce canonica `TI Program`, tipo `programming`, language_id `422`.

Show greeting with Disp in a TI program - BASIC exported as text.

## Toolchain and reproduction

Required genuine TI -Connect compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires TI tool that supports the exported text format and the calculator runtime.

Comando/procedura from the directory of the example, unless explicit indications:

```text
Importare hello.8xp.txt con uno strumento TI compatibile, tokenizzare nel formato .8xp e avviare HELLO su TI-83/84 o emulatore autentico.
```

Expected result: Hello, World! in the conformed result, according to the framework described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

The canon file. 8xp.txt contains original source with PROGRAM header and Disp instruction, not a false binary package. 8xp. Toolchain/calcolatrice absent.

Remaining requirements:

- Required TI-Connect toolchain and matching execution/format resources are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://education.ti.com/en/guidebook/details/en/BF077B5A987B41878D5FA83B6EADFBE5/84pceb](https://education.ti.com/en/guidebook/details/en/BF077B5A987B41878D5FA83B6EADFBE5/84pceb)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.8xp` | [hello.8xp](variants/8xp-e496e607/hello.8xp) syntax verified |
| `.8xp.txt` | [hello.8xp.txt](hello.8xp.txt) created; verification pending |
