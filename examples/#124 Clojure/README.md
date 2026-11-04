# #124 Clojure

Voce canonica: `Clojure`, tipo `programming`, `language_id: 62`.

Concatenate the two parts of the greeting in a binding let Clojure and print them with println.

## Toolchain and reproduction

Official Clojure JVM runtime, 1.12.0. Test environment: **Windows x64**.

Put in .tools official JAR chlojure 1.12.0, spec.alpha 0.5.238 and core.specs.alpha 0.4.74 from Maven Central. The wildcard classpath works with java on Windows and Linux. Try with Microsoft OpenJDK 21.0.12.1.

Comando/procedura from the example directory, except the build directory explicitly indicated:

```text
java -cp ".tools/*" clojure.main hello.clj
```

Exit 0; stdout exactly Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The authentic Clojure runtime reads and compiles the forms of the original file before executing them; the log binds the three JAR with SHA-256. Do not need a Leiningen project or a global installation of the CLI.

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

- [https://clojure.org/reference/repl_and_main](https://clojure.org/reference/repl_and_main)
- [https://clojure.org/reference/special_forms#let](https://clojure.org/reference/special_forms#let)
- [https://repo.maven.apache.org/maven2/org/clojure/clojure/1.12.0/](https://repo.maven.apache.org/maven2/org/clojure/clojure/1.12.0/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.clj` | [hello.clj](hello.clj) verified |
| `.bb` | [hello.bb](variants/ext-bb-2e6262/hello.bb) created; verification pending |
| `.boot` | [hello.boot](variants/ext-boot-2e626f6f74/hello.boot) created; verification pending |
| `.cl2` | [hello.cl2](variants/ext-cl2-2e636c32/hello.cl2) created; verification pending |
| `.cljc` | [hello.cljc](variants/ext-cljc-2e636c6a63/hello.cljc) created; verification pending |
| `.cljs` | [hello.cljs](variants/ext-cljs-2e636c6a73/hello.cljs) created; verification pending |
| `.cljs.hl` | [hello.cljs.hl](variants/ext-cljs-hl-2e636c6a732e686c/hello.cljs.hl) created; verification pending |
| `.cljscm` | [hello.cljscm](variants/ext-cljscm-2e636c6a73636d/hello.cljscm) created; verification pending |
| `.cljx` | [hello.cljx](variants/ext-cljx-2e636c6a78/hello.cljx) created; verification pending |
| `.hic` | [hello.hic](variants/ext-hic-2e686963/hello.hic) created; verification pending |
