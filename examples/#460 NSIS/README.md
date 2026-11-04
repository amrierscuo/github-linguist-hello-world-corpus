# #460 NSIS

Voce canonica `NSIS`, tipo `programming`, language_id `242`.

Fill out an original NSIS installer whose Section shows greeting and ends.

## Toolchain and reproduction

Official NSIS script compiler and native Windows installer generator, v3.09-4. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

NSIS 3.09-4 authentic with distribution stubs; compiler with cwd build to leave EXE out of the corpus.

Comando/procedura from the directory of the example, unless explicit indications:

```text
makensis -NOCD hello.nsi
```

Expected result: Exit 0, installer product; future UI would show Hello, World!.

## Status and evidence

Artifact **created**; syntax **verified**; behavioral verification **pending**.

Authentic Compiler produces a Windows installer, SHA in the log. For the agreed scope it is not executed or installed; behavior pending.

Remaining requirements:

- Installer script compiled; installer execution is intentionally not performed in this verification scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://nsis.sourceforge.io/Docs/Chapter4.html](https://nsis.sourceforge.io/Docs/Chapter4.html)
- [https://nsis.sourceforge.io/Docs/](https://nsis.sourceforge.io/Docs/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.nsi` | [hello.nsi](hello.nsi), [driver.nsi](variants/nsh-90f0ff9b/driver.nsi) created; verification pending |
| `.nsh` | [hello.nsh](variants/nsh-90f0ff9b/hello.nsh) created; verification pending |
