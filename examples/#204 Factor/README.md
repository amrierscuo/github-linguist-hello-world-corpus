# #204 Factor

Voce canonica `Factor`, tipo `programming`, language_id `108`.

Concatenate two strings on the Factor stack and print the greeting.

## Toolchain and reproduction

Required authentic toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64**.

It requires the VM of the Factor language and its immagine/librerie. Use the factorcode.org distribution executable, avoiding the homonymous GNU command of full factorization.

Comando/procedura from the directory of the example, unless explicit indications:

```text
factor hello.factor
```

Expected result: A Hello, World! line.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

USING imports me and sequences; hangs strings before print. VM is absent.

Remaining requirements:

- Factor language VM/image is unavailable; GNU coreutils factor would not verify Factor language.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sources verified in staging. The only available probe do not attest parsing
or execution. Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://factorcode.org/](https://factorcode.org/)
- [https://github.com/factor/factor](https://github.com/factor/factor)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.factor` | [hello.factor](hello.factor) created; verification pending |
