# #774 Witcher Script

Voce canonica `Witcher Script`, tipo `programming`, language_id `686821385`.

Original WitcherScript Global Function CorpusGreeting() that returns `Hello, World!` as string.

## Toolchain and reproduction

CD Projekt RED WitcherScript compiler / REDkit, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

You need the WitcherScript compiler of the game or REDkit, with compatible version.The manufacturer guide describes global functions, types and compile environment.

Comando/procedura from the directory of the example, unless explicit indications:

```text
In REDkit / The Witcher 3: aggiungere hello.ws a una mod di prova sotto content/scripts; compilare gli script; invocare CorpusGreeting() da un harness di debug e confrontare il risultato.
```

Expected result: Successful Compilation and CorpusGreeting() equal to Hello, World!.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Owner environment absent: the function is created, but no generic parser or read-only is used to mark positive verifications.

Remaining requirements:

- Compilatore/runtime WitcherScript e REDkit assenti.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://cdprojektred.atlassian.net/wiki/spaces/W3REDkit/pages/36306960/WitcherScript](https://cdprojektred.atlassian.net/wiki/spaces/W3REDkit/pages/36306960/WitcherScript)
- [https://cdprojektred.atlassian.net/wiki/spaces/W3REDkit/pages/36307090/WS+Language+Guide](https://cdprojektred.atlassian.net/wiki/spaces/W3REDkit/pages/36307090/WS+Language+Guide)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ws` | [hello.ws](hello.ws) created; verification pending |
