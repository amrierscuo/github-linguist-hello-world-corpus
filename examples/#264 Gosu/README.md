# #264 Gosu

Voce canonica `Gosu`, tipo `programming`, language_id `134`.

Define the Gosu Hello class with a main static that concatenates and prints greeting.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires the compatible compiler and runtime Gosu. Hello.gs is a Gosu class; use the distribution launcher to charge it and call the main, recording the actual command.

Comando/procedura from the directory of the example, unless explicit indications:

```text
Toolchain Gosu: aggiungere la directory della classe al classpath e invocare Hello.main(new String[0]) dal launcher/host della distribuzione
```

Expected result: Accepted class; main invocation emette Hello, World!.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

The official quickstart indicates Gosu Lab and a compatible JDK. The toolchain is not configured; the file is not interpreted as Groovy/Java.

Remaining requirements:

- Gosu compiler/runtime is not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://gosu-lang.github.io/quickstart.html](https://gosu-lang.github.io/quickstart.html)
- [https://github.com/gosu-lang/gosu-lang](https://github.com/gosu-lang/gosu-lang)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gs` | [Hello.gs](Hello.gs) created; verification pending |
| `.gst` | [hello.gst](variants/ext-gst-2e677374/hello.gst) created; verification pending |
| `.gsx` | [CorpusGreeting.gsx](variants/ext-gsx-2e677378/CorpusGreeting.gsx) created; verification pending |
| `.vark` | [hello.vark](variants/ext-vark-2e7661726b/hello.vark) created; verification pending |
