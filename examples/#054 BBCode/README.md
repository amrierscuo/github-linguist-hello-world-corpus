# #054 BBCode

Voce canonica: `BBCode`, tipo `markup`, `language_id: 206921123`.

Rendering the greeting BBCode as a bold text, obtaining HTML strong with Hello, World!.

## Toolchain and reproduction

Original dcwatson/bbcode Python parser/renderer, 1.1.0. Test environment: **Windows x64**.

Toolchain: Python 3.13.9 and parser/renderer dcwatson/bbcode 1.1.0. Here the dependence is isolated in work; for reproduction you can install it in a venv.

Comando/procedura from the example directory:

```text
python -m pip install bbcode==1.1.0; python verify.py hello.bbcode
```

Exit 0; <strong> Hello, World! </strong>; PASS of bold greeting and italic control.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

BBCode does not have a unique universal grammar. The positive state concerns the acceptance and surrender of b/i tags by this existing library, which is permissive; it is not a strict validator for all forums.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain and SHA-256 of artifacts. `path_normalization` describes the replacements of artifacts.
machine paths; source bytes remain those identified by checksums.
If the log only records the availability of the tools, no parsing or runtime is attested.
Tools, dependencies and verification products remain in the work directory.

## Primary sources

- [https://bbcode.readthedocs.io/en/latest/](https://bbcode.readthedocs.io/en/latest/)
- [https://github.com/dcwatson/bbcode](https://github.com/dcwatson/bbcode)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bbcode` | [hello.bbcode](hello.bbcode) verified |
