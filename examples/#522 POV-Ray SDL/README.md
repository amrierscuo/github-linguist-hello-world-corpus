# #522 POV-Ray SDL

Voce canonica `POV-Ray SDL`, tipo `programming`, language_id `275`.

Evaluate a SDL string and make a small POV -Ray original scene.

## Toolchain and reproduction

Original POV -Ray SDL parser and maker, POV -Ray 3.7.0.10 Ubuntu 3build4. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

POV-Ray 3.7.0.10 ufficiale, librerie SDL/runtime locali.

Comando/procedura from the directory of the example, unless explicit indications:

```text
povray +Ihello.pov +Obuild/hello.png +W16 +H16 -D +FN
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Greeting is a truly rated #debug directive, in addition to the sphere/camera/light scene; it is not a comment.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.povray.org/documentation/](https://www.povray.org/documentation/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pov` | [hello.pov](hello.pov), [driver.pov](variants/inc-dd126fb7/driver.pov) created; verification pending |
| `.inc` | [hello.inc](variants/inc-dd126fb7/hello.inc) created; verification pending |
