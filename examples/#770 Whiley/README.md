# #770 Whiley

Voce canonica `Whiley`, tipo `programming`, language_id `888779559`.

Pure Whiley function original greeting() that returns greeting as an array of entire code points, conforms to the string pattern of the Whiley specification.

## Toolchain and reproduction

Whiley Compiler / verification backend, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

The official guide documents wy init and wy build. No compiler has been installed for this item.

Comando/procedura from the directory of the example, unless explicit indications:

```text
In un progetto Whiley temporaneo: wy init; copiare hello.whiley in src/hello.whiley; wy build; valutare hello.greeting() con il runtime Whiley.
```

Expected result: 13 code point array corresponding to Hello, World!.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Source created from specification: the reading of the file is not counted as a syntactic verification.

Remaining requirements:

- Whiley compiler and backend verification absents; pure function defined but not compiled.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://whiley.org/pdfs/WhileyLanguageSpec.pdf](https://whiley.org/pdfs/WhileyLanguageSpec.pdf)
- [https://whiley.org/learn/](https://whiley.org/learn/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.whiley` | [hello.whiley](hello.whiley) created; verification pending |
