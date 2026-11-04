# #214 Formatted

Voce canonica `Formatted`, tipo `data`, language_id `113`.

Represent greeting as a field of a fixed-width record and read it with an existing parser according to the stated layout.

## Toolchain and reproduction

Existing NumPy genfromtxt fixed-width record parser, 2.3.5. Test environment: **Windows x64**.

NumPy 2.3.5 on Python 3.13.9. Original layout: full id of 3 columns, greeting of 13 columns, full length of 4 columns; each record ends with LF.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python -m pip install numpy==2.3.5; python verify.py hello.for
```

Expected result: A record: id= 1, greeting Hello, World!, length= 13; PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Formatted is a wide range of data in the Linguist baseline: the samples include reports and tables with different formats. The positive flags concern only this explicit layout read by numpy.genfromtxt; no universal grammar is attributed to the category, no EAM/Finnis–Sinclair validity to this file.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sources verified in staging. The only available probe do not attest parsing
or execution. Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/github-linguist/linguist/tree/main/samples/Formatted](https://github.com/github-linguist/linguist/tree/main/samples/Formatted)
- [https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.for` | [hello.for](hello.for) verified |
| `.eam.fs` | [hello.eam.fs](variants/ext-eam-fs-2e65616d2e6673/hello.eam.fs) created; verification pending |
