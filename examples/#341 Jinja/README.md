# #341 Jinja

Voce canonica `Jinja`, tipo `markup`, language_id `147`.

Fill out a parametric Jinja template and check the greeting for World, Reader and missing parameter.

## Toolchain and reproduction

Official Jinja compiler/runtime, jinja2 3.1.6. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Jinja 3.1.6 official already present on Python 3.13.9. Environment uses StrictUndefined and keep_trailing_newline=True.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python verify.py hello.jinja
```

Expected result: Hello, World! and PASS of parametric controls.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The real engine compiles the template and makes two exact values. The absence of the parameter must lift UndefinedError. No alternative template engine is used.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://jinja.palletsprojects.com/en/stable/api/](https://jinja.palletsprojects.com/en/stable/api/)
- [https://jinja.palletsprojects.com/en/stable/templates/](https://jinja.palletsprojects.com/en/stable/templates/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.jinja` | [hello.jinja](hello.jinja) verified |
| `.j2` | [hello.j2](variants/j2-d70c3c7d/hello.j2) syntax and behavior verified |
| `.jinja2` | [hello.jinja2](variants/jinja2-dda60d41/hello.jinja2) syntax and behavior verified |

## Additional extension verification

- `.j2`: verified on November 4, 2026. [Evidence](verification/native_20261104_341_variants_result.json).
- `.jinja2`: verified on November 4, 2026. [Evidence](verification/native_20261104_341_variants_result.json).
