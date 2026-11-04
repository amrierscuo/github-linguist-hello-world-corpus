# #536 PigLatin

Voce canonica `PigLatin`, tipo `programming`, language_id `286`.

Upload a local TSV and turn World into a PigLatin record with greeting.

## Toolchain and reproduction

Required genuine compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires Apache Pig 0.17.0 and runtime Java/Hadoop compatible for execution local.

Comando/procedura from the directory of the example, unless explicit indications:

```text
pig -x local hello.pig
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

LOAD, FOREACH GENERATE e CONCAT originali. DUMP deve mostrare (Hello, World!); toolchain locale non configurata.

Remaining requirements:

- Required pig compiler/interpreter and matching host libraries are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://pig.apache.org/docs/r0.17.0/basic.html](https://pig.apache.org/docs/r0.17.0/basic.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pig` | [hello.pig](hello.pig) created; verification pending |
