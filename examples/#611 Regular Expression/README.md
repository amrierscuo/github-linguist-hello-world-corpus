# #611 Regular Expression

## Latest recorded verification

Latest extension checks:
- `.regex`: CPython re engine: exact named capture, rejection controls. [Evidence](verification/native_20261104_followup_2e7265676578.json).

Voce canonica `Regular Expression`, tipo `data`, language_id `363378884`.

Fill out a Python regex that recognizes World greeting and captures.

## Toolchain and reproduction

Python standard-library re regular expression engine, 3.13.9. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python 3.13.9 re nativo; dialetto dichiarato con named group (?P<name>...).

Comando/procedura from the directory of the example, unless explicit indications:

```text
python verify.py
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Fullmatch valid and Reader/punteggiatura extra controls rejected by the real engine.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.regexp` | [hello.regexp](hello.regexp) verified |
| `.regex` | [hello.regex](variants/regex-b64e0ba7/hello.regex) syntax and behavior verified |