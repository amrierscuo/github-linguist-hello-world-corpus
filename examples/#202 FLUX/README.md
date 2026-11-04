# #202 FLUX

Voce canonica `FLUX`, tipo `programming`, language_id `106`.

Define in UMass FLUX a GetGreeting source and a PrintGreeting node connected by a stream; C++ implementations print the first event and end.

## Toolchain and reproduction

Required authentic toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64**.

Requires the historical Java compiler of emeryberger/flux, distribution dependencies and the generated C++ driver. Follow the upstream procedure for the backend thread. mImpl.h is produced by the generator and is not invented in the corpus.

Comando/procedura from the directory of the example, unless explicit indications:

```text
Nel checkout ufficiale Flux: ant; java -cp bin:lib/jdsl.jar:lib/javacuplex.jar:lib/getopt.jar edu.umass.cs.flux.Main -r build/server -t hello.fx; copiare mImpl.cpp nel server generato; compilare il server C++ generato con pthread; eseguirlo
```

Expected result: Generazione/compilazione successful; server outputs a Hello, World! line and ends 0.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

This entry is FLUX for high performance servers and task streams. GetGreeting_out and PrintGreeting_in signatures follow the original backend. The termination after the first event avoids an unlimited source loop; without toolchain are not attributed positive flags.

Remaining requirements:

- Historical UMass Flux Java compiler and generated C++ runtime are not built; mImpl.cpp depends on generated mImpl.h.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sources verified in staging. The only available probe do not attest parsing
or execution. Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/emeryberger/flux](https://github.com/emeryberger/flux)
- [https://www.usenix.org/legacy/event/usenix06/tech/full_papers/burns/burns_html/__flux-usenix-06.html](https://www.usenix.org/legacy/event/usenix06/tech/full_papers/burns/burns_html/__flux-usenix-06.html)
- [https://github.com/github-linguist/linguist/tree/main/samples/FLUX](https://github.com/github-linguist/linguist/tree/main/samples/FLUX)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.fx` | [hello.fx](hello.fx) created; verification pending |
| `.flux` | [hello.flux](variants/ext-flux-2e666c7578/hello.flux) created; verification pending |
