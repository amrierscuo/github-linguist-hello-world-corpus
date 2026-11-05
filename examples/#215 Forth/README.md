# #215 Forth

## Latest recorded verification

Latest extension checks:
- `.4th`: Gforth loaded its original VM image, compiled and executed the exact suffix variant, and printed exactly Hello, World! plus LF without stderr. [Evidence](verification/native_20261105_batch_2e347468.json).
- `.f`: Gforth loaded its original VM image, compiled and executed the exact suffix variant, and printed exactly Hello, World! plus LF without stderr. [Evidence](verification/native_20261105_batch_2e66.json).
- `.for`: Gforth loaded its original VM image, compiled and executed the exact suffix variant, and printed exactly Hello, World! plus LF without stderr. [Evidence](verification/native_20261105_batch_2e666f72.json).
- `.forth`: Gforth loaded its original VM image, compiled and executed the exact suffix variant, and printed exactly Hello, World! plus LF without stderr. [Evidence](verification/native_20261105_batch_2e666f727468.json).
- `.fr`: Gforth loaded its original VM image, compiled and executed the exact suffix variant, and printed exactly Hello, World! plus LF without stderr. [Evidence](verification/native_20261105_batch_2e6672.json).
- `.frt`: Gforth loaded its original VM image, compiled and executed the exact suffix variant, and printed exactly Hello, World! plus LF without stderr. [Evidence](verification/native_20261105_batch_2e667274.json).
- `.fs`: Gforth loaded its original VM image, compiled and executed the exact suffix variant, and printed exactly Hello, World! plus LF without stderr. [Evidence](verification/native_20261105_batch_2e6673.json).

Voce canonica `Forth`, tipo `programming`, language_id `114`.

Define the word Forth greet, write greetings with." and finish the interpreter.

## Toolchain and reproduction

Gforth native interpreter and original gforth.fi image, gforth 0.7.3. Test environment: **Ubuntu 24.04 WSL2/Linux x86_64**.

Gforth 0.7.3, with the original engine and gforth.fi image of the Ubuntu distribution.

Comando/procedura from the directory of the example, unless explicit indications:

```text
gforth hello.fth
```

Exit 0; exact greeting followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

La parola viene realmente compilata nell’interprete Forth e poi eseguita; cr aggiunge newline e bye termina con successo.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sources verified in staging. The only available probe do not attest parsing
or execution. Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.complang.tuwien.ac.at/forth/gforth/Docs-html/](https://www.complang.tuwien.ac.at/forth/gforth/Docs-html/)
- [https://forth-standard.org/standard/core/Dotp](https://forth-standard.org/standard/core/Dotp)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.fth` | [hello.fth](hello.fth) verified |
| `.4th` | [hello.4th](variants/ext-4th-2e347468/hello.4th) syntax and behavior verified |
| `.f` | [hello.f](variants/ext-f-2e66/hello.f) syntax and behavior verified |
| `.for` | [hello.for](variants/ext-for-2e666f72/hello.for) syntax and behavior verified |
| `.forth` | [hello.forth](variants/ext-forth-2e666f727468/hello.forth) syntax and behavior verified |
| `.fr` | [hello.fr](variants/ext-fr-2e6672/hello.fr) syntax and behavior verified |
| `.frt` | [hello.frt](variants/ext-frt-2e667274/hello.frt) syntax and behavior verified |
| `.fs` | [hello.fs](variants/ext-fs-2e6673/hello.fs) syntax and behavior verified |