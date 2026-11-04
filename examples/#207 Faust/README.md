# #207 Faust

Voce canonica `Faust`, tipo `programming`, language_id `622529198`.

Generate a DSP Faust with thirteen constant channels ASCII and rebuild greeting from a truly calculated audio frame.

## Toolchain and reproduction

Official Faust compiler extracted from Ubuntu package, Faust 2.70.3; GCC 13.3.0. Test environment: **Ubuntu 24.04 WSL2/Linux x86_64**.

Faust 2.70.3 and GNU G++ 13.3.0 on Ubuntu. For locally extracted distribution, use LD_LIBRARY_PATH of Faust libraries. The generated file and the track remain in the build directory.

Comando/procedura from the directory of the example, unless explicit indications:

```text
faust -lang cpp -cn GreetingDSP -o build/GreetingDSP.h hello.dsp; g++ -std=c++17 -O2 -I build verify.cpp -o build/check; ./build/check
```

Expected result: Hello, World! and PASS of the assertions on the samples.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

verify.cpp provides the interfaces of the DSP architecture and invokes init/compute of the authentically generated code. It controls zero inputs, thirteen outputs and thirteen ASCII samples; it does not rewrite the DSP logic in C++.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sources verified in staging. The only available probe do not attest parsing
or execution. Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://faustdoc.grame.fr/manual/syntax/](https://faustdoc.grame.fr/manual/syntax/)
- [https://faustdoc.grame.fr/manual/compiler/](https://faustdoc.grame.fr/manual/compiler/)
- [https://faustdoc.grame.fr/manual/architectures/](https://faustdoc.grame.fr/manual/architectures/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.dsp` | [hello.dsp](hello.dsp) verified |
