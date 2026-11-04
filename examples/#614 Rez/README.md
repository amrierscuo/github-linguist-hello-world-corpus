# #614 Rez

Voce canonica `Rez`, tipo `programming`, language_id `498022874`.

Fill out an original Mac Rez TEXT resource with greeting in the payload.

## Toolchain and reproduction

Required genuine Rez compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires Apple Rez/DeRez and Types.r template of SDK Mac compatible.

Comando/procedura from the directory of the example, unless explicit indications:

```text
Rez -i /path/to/MacSDK/RezHeaders hello.r -o build/hello.rsrc; DeRez -only TEXT build/hello.rsrc
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Resource id 128 e payload originali; toolchain Apple assente.

Remaining requirements:

- Required Rez compiler/runtime and matching host resources are not available/configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/Cpp/Resources/Resources.html](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/Cpp/Resources/Resources.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.r` | [hello.r](hello.r) created; verification pending |
