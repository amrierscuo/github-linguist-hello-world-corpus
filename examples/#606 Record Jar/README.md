# #606 Record Jar

Voce canonica `Record Jar`, tipo `data`, language_id `865765202`.

Read an original Record Jar in the registry format of language subtags.

## Toolchain and reproduction

Existing language_data authentic format parser, 1.4.0. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

language-data 1.4.0 e suo registry_parser.parse_file esistente.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python verify.py
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

An original private-use qaaa fixture contains Description Hello, World!. It does not appear as an authoritative copy IANA. The real parser decodifies header, separator and record, compared to the helper.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.rfc-editor.org/rfc/rfc5646#section-3.1.1](https://www.rfc-editor.org/rfc/rfc5646#section-3.1.1)
