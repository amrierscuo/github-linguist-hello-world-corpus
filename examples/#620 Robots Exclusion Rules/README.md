# #620 Robots Exclusion Rules

Voce canonica `Robots Exclusion Rules`, tipo `data`, language_id `674736065`.

Verify a robots.txt policy that admits the greeting file and blocks a private path.

## Toolchain and reproduction

Python standard-library urllib.robotparser policy engine, 3.13.9. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

urllib.robotparser Python standard library; file e target locale originali.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python verify.py
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The real parser admits / hello.txt and refuses / private/file for CorpusBot. The target contains greeting; no network access and no hosting.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.rfc-editor.org/rfc/rfc9309](https://www.rfc-editor.org/rfc/rfc9309)
