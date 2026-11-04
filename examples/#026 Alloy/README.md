# #026 Alloy

Voce canonica: `Alloy`, tipo `programming`, `language_id: 13`.
`hello.als` binds a single `Greeting` to have the `Hello, World!` text,
requires an instance with `run showGreeting` and controls the statement on the text
con `check GreetingIsHelloWorld`, entrambi entro scope 3.

## Toolchain and reproduction

verified su Windows x64 con **Alloy 6.2.0**, solver **SAT4J** incluso e
**Microsoft OpenJDK 21.0.12.1**. You need a JDK for the launch of the Java source.
Download the official JAR from Maven Central into the local `.tools` directory, then:

```powershell
java -version
java -jar .tools/alloy-6.2.0.jar version
java -jar .tools/alloy-6.2.0.jar commands hello.als
java -Dorg.slf4j.simpleLogger.defaultLogLevel=error --class-path .tools/alloy-6.2.0.jar AlloyCheck.java hello.als
```

Artefatto Maven: `org.alloytools:org.alloytools.alloy.dist:6.2.0`.
The JAR is called `org.alloytools.alloy.dist-6.2.0.jar` at the source; rename it
locally `alloy-6.2.0.jar` for the commands above. SHA-256 verified in the log:
`6037cbeee0e8423c1c468447ed10f5fcf2f2743a2ffc39cb1c81f2905c0fdb9d`.

`AlloyCheck.java` is an original harness: parsing delegation, typecheck, translation
and solution to API Official Alloy. Expected result: `showGreeting: SAT` with
unico atomo stringa `"Hello, World!"`, `GreetingIsHelloWorld: UNSAT counterexample,
broom 3 `, e ` PASS ` for all assertions. Includes negative control of the
signature malformed rejected by the royal parser.

## Status and evidence

Artefatto created; syntax **verified**; behavior **verified** con SAT4J.
The absence of counterexamples is attested within the specified broom, not beyond the
search limits. Field assessment controls the instance string
the previous `exec` CLI had finished without producing a return;
the only 0 code of that command was not used as behavior test.
No residual requirement for verification within broom 3.

Log: [alloy.json](verification/alloy.json), with commands, API output,
version and SHA-256 of artifacts. `path_normalization` documents the routes
normalized; the sources and results of the solver remain unchanged.

## Official sources

- [Documentazione e API Alloy](https://alloytools.org/documentation.html).
- [Distribuzione e requisiti](https://github.com/AlloyTools/org.alloytools.alloy).
- [JAR ufficiale Maven Central 6.2.0](https://repo.maven.apache.org/maven2/org/alloytools/org.alloytools.alloy.dist/6.2.0/).

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.als` | [hello.als](hello.als) verified |
