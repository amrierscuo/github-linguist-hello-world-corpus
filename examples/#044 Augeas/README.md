# #044 Augeas

Voce canonica: `Augeas`, tipo `programming`, `language_id: 25`.

Map Hello, World! followed by newline in the Augeas greeting node, then check the round trip get/put.

## Toolchain and reproduction

augparse / libaugeas Ubuntu package extracted locally, augparse 1.14.1 < http://augeas.net/ >. Test environment: **Ubuntu 24.04 WSL2/Linux x86_64**.

Requires Augeas augparse and standard modules of the same version. The test uses Ubuntu 1.14.1 packages extracted in local work and LD_LIBRARY_PATH, without system installation.

Comando/procedura from the example directory:

```text
augparse -I . hello.aug
```

Exit 0; test get produces { Hello, World! }; put test reconstructs Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The source contains an original lens and two native tests. augparse tests types and tests; the regex of greeting does not replace the parser of the language, is part of the lens itself.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain and SHA-256 of artifacts. `path_normalization` describes the replacements of artifacts.
machine paths; source bytes remain those identified by checksums.
If the log only records the availability of the tools, no parsing or runtime is attested.
Tools, dependencies and verification products remain in the work directory.

## Primary sources

- [https://augeas.net/docs/lenses.html](https://augeas.net/docs/lenses.html)
- [https://augeas.net/docs/language.html](https://augeas.net/docs/language.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.aug` | [hello.aug](hello.aug) verified |
