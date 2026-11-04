# #048 Awk

Voce canonica: `Awk`, tipo `programming`, `language_id: 28`.

Perform the BEGIN Awk block without input and print the concatenate greeting.

## Toolchain and reproduction

GNU Awk: GNU Awk 5.2.1, API 3.2, PMA Avon 8-g1, (GNU MPFR 4.2.1, GNU MP 6.3.0). Test environment: **Ubuntu 24.04 WSL2/Linux x86_64**.

Requires GNU Awk 5.2.1; test performed in Ubuntu 24.04 WSL2.

Comando/procedura from the example directory:

```text
gawk -f hello.awk
```

Exit 0; stdout Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The Awk concatenation is expressed by flanking strings; BEGIN performs the program before reading the records.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain and SHA-256 of artifacts. `path_normalization` describes the replacements of artifacts.
machine paths; source bytes remain those identified by checksums.
If the log only records the availability of the tools, no parsing or runtime is attested.
Tools, dependencies and verification products remain in the work directory.

## Primary sources

- [https://www.gnu.org/software/gawk/manual/gawk.html](https://www.gnu.org/software/gawk/manual/gawk.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.awk` | [hello.awk](hello.awk) verified |
| `.auk` | [hello.auk](variants/ext-auk-2e61756b/hello.auk) created; verification pending |
| `.gawk` | [hello.gawk](variants/ext-gawk-2e6761776b/hello.gawk) created; verification pending |
| `.mawk` | [hello.mawk](variants/ext-mawk-2e6d61776b/hello.mawk) created; verification pending |
| `.nawk` | [hello.nawk](variants/ext-nawk-2e6e61776b/hello.nawk) created; verification pending |
