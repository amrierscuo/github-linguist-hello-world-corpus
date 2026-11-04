# #690 Survex data

Voce canonica `Survex data`, tipo `data`, language_id `24470517`.

Process an original Survex measurement and read titles and stations from its 3d. model

## Toolchain and reproduction

Official Survex Cavern survey processor and dump3d reader, <workspace>/ work/tools_681_700/linux/usr/bin/cavern - Survex 1.4.4. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Survex 1.4.4 authentic and PROJ9.4 local. PRoot5.1.0 map only in the view of the process the message files extracted under / usr/share/survex, without installation or global writing.

Comando/procedura from the directory of the example, unless explicit indications:

```text
cavern -o build/hello.3d hello.svx; dump3d build/hello.3d
```

Expected result: Hello, World! in the conformed result, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Il titolo Hello, World! eÌâ‚¬ metadata della survey; i dati contengono un ingresso fissato e una camera misurata. Cavern e dump3d autentici producono/leggono il modello.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://survex.com/docs/manual/cavern.htm](https://survex.com/docs/manual/cavern.htm)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.svx` | [hello.svx](hello.svx) verified |
