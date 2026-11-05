# #218 FreeBASIC

## Latest recorded verification

**Syntax and behavior verified** on November 5, 2026.

Authentic FreeBASIC compiled the unchanged main and original .bi include consumer; both native executables printed exactly Hello, World!. Required compatibility libraries were extracted locally without system installation.

[Native commands, versions, outputs and SHA-256](verification/native_20261105_target546_main.json). [Earlier evidence](verification/native.json).

Current native command or procedure: `fbc hello.bas -x hello; ./hello (also compile/run the original .bi consumer as recorded)`.

## Extension results

- `.bas`: syntax and behavior verified.
- `.bi`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

Voce canonica `FreeBASIC`, tipo `programming`, language_id `472896659`.

Concatenare stringhe FreeBASIC e stamparle con Print.

## Toolchain and reproduction

Required authentic toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64**.

Requires FreeBASIC fbc compiler and its compatible runtime. The compiler is not present in this environment.

Comando/procedura from the directory of the example, unless explicit indications:

```text
fbc hello.bas -x build/hello; ./build/hello
```

Exit 0; Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Dim As String, concatenation + and End 0 are original FreeBASIC source; an execution with a different BASIC is not attested.

Remaining requirements:

- FreeBASIC native fbc compiler is unavailable.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sources verified in staging. The only available probe do not attest parsing
or execution. Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.freebasic.net/wiki/KeyPgPrint](https://www.freebasic.net/wiki/KeyPgPrint)
- [https://www.freebasic.net/wiki/KeyPgString](https://www.freebasic.net/wiki/KeyPgString)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bi` | [hello.bi](variants/ext-bi-2e6269/hello.bi) syntax and behavior verified |
| `.bas` | [hello.bas](hello.bas), [consumer.bas](variants/ext-bi-2e6269/consumer.bas) syntax and behavior verified |

</details>
