# #212 Flix

Voce canonica `Flix`, tipo `programming`, language_id `800935960`.

Check the Flix program tipi/effetti and print a concatenation in the main with IO effect.

## Toolchain and reproduction

Official Flix compiler and JVM code generator, The Flix Programming Language 0.77.0. Test environment: **Windows x64**.

Official Flix 0.77.0 and JDK 21. The initialization creates the work project; maintain one main definition. check/run commands operate on the project and do not accept the same file arguments.

Comando/procedura from the directory of the example, unless explicit indications:

```text
In una copia di lavoro: java -jar flix.jar init; sostituire src/Main.flix con Main.flix; java -jar flix.jar check --no-install --threads 2; java -jar flix.jar run --no-install --threads 2
```

Expected result: Check exit 0; run exit 0; stdout Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The log attests successful check and run on the project containing an identical copy of the source.The resolution of the initialized project dependencies produces diagnostics on stderr, without preventing execution.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sources verified in staging. The only available probe do not attest parsing
or execution. Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://doc.flix.dev/getting-started.html](https://doc.flix.dev/getting-started.html)
- [https://doc.flix.dev/build-and-packages.html](https://doc.flix.dev/build-and-packages.html)
- [https://flix.dev/](https://flix.dev/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.flix` | [Main.flix](Main.flix) verified |
