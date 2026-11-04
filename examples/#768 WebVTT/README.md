# #768 WebVTT

Voce canonica `WebVTT`, tipo `data`, language_id `658679714`.

Sottotitolo WebVTT originale, identificatore greeting: `Hello, World!` nell’intervallo da 0 a 2 secondi.

## Toolchain and reproduction

webvtt-py / Python 3.13.9, 0.5.1. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python 3.13.9 e webvtt-py 0.5.1 in ambiente isolato.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python verify.py
```

Expected result: Hello, World! and PASS for 0 to 2 seconds.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The existing WebVTT decoder reads the cue; the driver controls the times and the text. The test covers the data model of the caption, without attesting the rendering of a player.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.w3.org/TR/webvtt1/](https://www.w3.org/TR/webvtt1/)
- [https://github.com/glut23/webvtt-py](https://github.com/glut23/webvtt-py)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.vtt` | [hello.vtt](hello.vtt) verified |
