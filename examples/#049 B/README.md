# #049 B

Voce canonica: `B`, tipo `programming`, `language_id: 700792152`.

Enter the ASCII characters of Hello, World! one at a time via the putchar library of the historical language B.

## Toolchain and reproduction

b, unavailable / not verified. Test environment: **Windows x64**.

It requires a toolchain of Ken Thompson's historic B and his putchar library. No toolchain B has been found; it is not compiled as C.

Comando/procedura from the example directory:

```text
Compilatore storico B: compilare hello.b con la libreria che espone putchar; eseguire il programma risultante (comando specifico da registrare quando disponibile).
```

Expected result: successful B compilation; stdout Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

extrn declares the external function. Newline uses the B*n convention. The program avoids assumptions on the packed layout of B strings; calls work with individual characters.

Remaining requirements:

- b toolchain not installed or not available in this isolated verification environment.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain and SHA-256 of artifacts. `path_normalization` describes the replacements of artifacts.
machine paths; source bytes remain those identified by checksums.
If the log only records the availability of the tools, no parsing or runtime is attested.
Tools, dependencies and verification products remain in the work directory.

## Primary sources

- [https://www.bell-labs.com/usr/dmr/www/btut.pdf](https://www.bell-labs.com/usr/dmr/www/btut.pdf)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.b` | [hello.b](hello.b) created; verification pending |
