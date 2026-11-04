# #220 Frege

Voce canonica `Frege`, tipo `programming`, language_id `116`.

Fill out the Frege Hello functional module in bytecode JVM and invoke the main.

## Toolchain and reproduction

Official Frege compiler and runtime JVM jar — 3.25.153; commit 2abfb8f17a795185503b537625afc0cd57e1fac9; Merge: 067cad05 ea4fe246; Author: Ingo Wechsung ; Date:   Sat Jul 11 10:33:45 2026 +0200; ;     Merge pull request #401 from poeik/native-gen-fixes;     ;     Native gen fixes. Ambiente della prova: **Windows x64**.

Official 3.25.153 and JDK 21 on Windows. On Linux the classpath separator is: instead of;. Java generated and classes remain in build.

Comando/procedura from the directory of the example, unless explicit indications:

```text
java -jar .tools/frege-3.25.153.jar -d build Hello.fr; java -cp ".tools/frege-3.25.153.jar;build" Hello
```

Expected result: Compiler exit 0; Hello exit 0 execution and exact greeting.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Il compiler Frege ha prodotto e compilato il vero Java; il secondo comando esegue quelle classi con il runtime Frege. Non viene eseguito un equivalente Java scritto a mano.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sources verified in staging. The only available probe do not attest parsing
or execution. Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/Frege/frege](https://github.com/Frege/frege)
- [https://github.com/Frege/frege/wiki/Getting-Started](https://github.com/Frege/frege/wiki/Getting-Started)
- [https://repo.maven.apache.org/maven2/org/frege-lang/frege/3.25.153/](https://repo.maven.apache.org/maven2/org/frege-lang/frege/3.25.153/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.fr` | [Hello.fr](Hello.fr) verified |
