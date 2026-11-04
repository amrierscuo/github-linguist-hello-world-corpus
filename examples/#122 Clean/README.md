# #122 Clean

Voce canonica: `Clean`, tipo `programming`, `language_id: 60`.

Open the stream console through the world unique Clean, concatenate greeting, write it and close the stream.

## Toolchain and reproduction

Clean 3.1 stable distribution, local clm, 3.1. Test environment: **Ubuntu 24.04 WSL2/Linux x86_64**.

Distribuzione ufficiale Clean 3.1 Linux x86_64, installata con make in una directory di lavoro. Se clm non risolve i percorsi interni, impostare CLEANLIB=<clean>/lib/exe, CLEANPATH=<clean>/lib/StdEnv e CLEANILIB=<clean>/lib. Compilare una copia di Hello.icl: clm crea i suoi prodotti accanto al modulo.

Comando/procedura from the example directory, except the build directory explicitly indicated:

```text
clm -nr -nt -nw Hello -o hello; ./hello
```

Expected result: Successful compilation; stdout exactly Hello, World! followed by LF.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Start passes the *World value to stdio and fclose, respecting the discipline of uniqueness. -nr disables the automatic print of the world final value by the runtime; -nt disables timing.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain versions and SHA-256 values for the artifacts. The `path_normalization` property documents
local route replacements. `<corpus>` identifies the relative files included in
final corpus, which were first verified in the staging directory.
sources remain those identified by checksums. The only offspring of availability
instruments do not attest parsing or execution.
in the work directory and are not included in the corpus.

## Primary sources

- [https://clean.cs.ru.nl/Download_Clean](https://clean.cs.ru.nl/Download_Clean)
- [https://clean.cs.ru.nl/*NIX_Instructions](https://clean.cs.ru.nl/*NIX_Instructions)
- [https://clean.cs.ru.nl/Clean_language_report](https://clean.cs.ru.nl/Clean_language_report)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.icl` | [Hello.icl](Hello.icl), [Consumer.icl](variants/ext-dcl-2e64636c/Consumer.icl), [Greeting.icl](variants/ext-dcl-2e64636c/Greeting.icl) created; verification pending |
| `.dcl` | [Greeting.dcl](variants/ext-dcl-2e64636c/Greeting.dcl) created; verification pending |
