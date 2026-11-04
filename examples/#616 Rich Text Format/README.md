# #616 Rich Text Format

Voce canonica `Rich Text Format`, tipo `markup`, language_id `51601661`.

Decode an original Rich Text Format document in plain text greeting.

## Toolchain and reproduction

Existing striprtf authentic format parser, 0.0.33. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Parser esistente striprtf 0.0.33.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python verify.py
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Il parser reale interpreta rtf1, font table, f0 e par: confronto del corpo decodificato. Il goal eÌ€ estrazione testuale, non impaginazione grafica.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://learn.microsoft.com/en-us/previous-versions/office/developer/office2007/aa338117(v=office.12)](https://learn.microsoft.com/en-us/previous-versions/office/developer/office2007/aa338117(v=office.12))

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.rtf` | [hello.rtf](hello.rtf) verified |
