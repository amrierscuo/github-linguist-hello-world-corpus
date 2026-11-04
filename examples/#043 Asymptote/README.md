# #043 Asymptote

Voce canonica: `Asymptote`, tipo `programming`, `language_id: 591605007`.

Concatenate Hello, and World! and write greetings on stdout Asymptote.

## Toolchain and reproduction

Asymptote interpreter distributed with MiKTeX, miktex-asy version 2.88 [(C) 2004 Andy Hammerlindl, John C. Bowman, Tom Prince]. Test environment: **Windows x64**.

It requires Asymptote and a consistent distribution of its standard modules. It does not use graphics, TeX or a viewer: the program only invokes write on a string.

Comando/procedura from the example directory:

```text
asy -noV hello.asy
```

Exit 0; stdout Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

The local MiKTeX interpreter has actually been executed, but it does not charge the plain module: the log shows errors on the standard modules before the source is executed. A consistent toolchain is needed; syntax and behavior remain false.

Remaining requirements:

- Asymptote interpreter runs, but local MiKTeX standard plain modules produce compiler errors; coherent interpreter/library installation required.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain and SHA-256 of artifacts. `path_normalization` describes the replacements of artifacts.
machine paths; source bytes remain those identified by checksums.
If the log only records the availability of the tools, no parsing or runtime is attested.
Tools, dependencies and verification products remain in the work directory.

## Primary sources

- [https://asymptote.sourceforge.io/doc/Files.html](https://asymptote.sourceforge.io/doc/Files.html)
- [https://asymptote.sourceforge.io/doc/Options.html](https://asymptote.sourceforge.io/doc/Options.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.asy` | [hello.asy](hello.asy) created; verification pending |
