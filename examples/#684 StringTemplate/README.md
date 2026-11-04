# #684 StringTemplate

Voce canonica `StringTemplate`, tipo `markup`, language_id `89855901`.

Compilare/renderizzare a StringTemplate template with name parameter.

## Toolchain and reproduction

Official StringTemplate Java compiler/renderer ST4 4.3.4 / ANTLR runtime 3.5.3.

Java 21, ST4 4.3.4 and ANTLR runtime 3.5.3. The classpath separator shown is the Windows test; on Linux use the two points. The Verify.java driver reads hello.st from the current directory.

```text
java -cp "/path/ST4-4.3.4.jar;/path/antlr-runtime-3.5.3.jar" Verify.java
```

Expected result: Driver ST4 exit 0; rendering World and Reader conforms. The comparison ignores only the space at the edges.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Un commento valido StringTemplate descrive il parametro name. ST4 riconosce il commento, lo elimina dal rendering e verifica nativamente sia World sia Reader con il driver Java invariato. Il commento identifica il template rispetto agli altri linguaggi .st.

Current evidence: [recognition.json](verification/recognition.json), with a UTC timestamp, native commands, exit codes, stdout/stderr, toolchain details and SHA-256 values for modified sources and drivers. Earlier evidence is retained as history. Expected Linguist classification is distinct from the statistics actually observed on GitHub. This batch applies no language override.

## Primary sources

- https://www.stringtemplate.org/
- https://github.com/antlr/stringtemplate4/blob/master/doc/templates.md
- https://github.com/github-linguist/linguist/blob/v9.7.0/lib/linguist/heuristics.yml

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.st` | [hello.st](hello.st) syntax and behavior verified |
