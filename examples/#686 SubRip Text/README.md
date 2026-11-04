# #686 SubRip Text

Voce canonica `SubRip Text`, tipo `data`, language_id `360`.

Decode a SubRip subtitling with greeting and interval of two seconds.

## Toolchain and reproduction

Existing PySRT format parser, 1.1.2. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Parser esistente pysrt 1.1.2.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python verify.py
```

Expected result: Hello, World! in the conformed result, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The real decoder valid index, start/end and text; the goal is the subtitle model, without video-player.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/byroot/pysrt](https://github.com/byroot/pysrt)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.srt` | [hello.srt](hello.srt) verified |
