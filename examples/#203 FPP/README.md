# #203 FPP

Voce canonica `FPP`, tipo `programming`, language_id `252360067`.

Declare a constant Greeting string in the Corpus module of the NASA FPP language.

## Toolchain and reproduction

Required authentic toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64**.

Richiede gli strumenti autentici NASA FPP. La build corrente upstream usa Scala/sbt e JDK 25; non sono configurati qui. Il modello è una dichiarazione FPP, quindi l’obiettivo è il valore della costante, non un processo console autonomo.

Comando/procedura from the directory of the example, unless explicit indications:

```text
fpp-check hello.fpp; fpp-to-xml -d build hello.fpp
```

Expected result: FPP accepted; constant Corpus.Greeting equal to Hello, World!.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Greeting is the actual value of the constant. No XML or YAML generic replaces fpp-check.

Remaining requirements:

- FPP analysis/translation tools are unavailable; current upstream build requires Scala sbt and JDK 25.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sources verified in staging. The only available probe do not attest parsing
or execution. Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://nasa.github.io/fpp/fpp-spec.html](https://nasa.github.io/fpp/fpp-spec.html)
- [https://nasa.github.io/fpp/fpp-users-guide.html](https://nasa.github.io/fpp/fpp-users-guide.html)
- [https://github.com/nasa/fpp](https://github.com/nasa/fpp)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.fpp` | [hello.fpp](hello.fpp), [consumer.fpp](variants/ext-fppi-2e66707069/consumer.fpp) created; verification pending |
| `.fppi` | [hello.fppi](variants/ext-fppi-2e66707069/hello.fppi) created; verification pending |
