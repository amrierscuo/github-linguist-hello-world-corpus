# 0529: Pascal: `.dpr`

Ruolo: Programma Delphi console con direttiva APPTYPE; mantiene entry point program.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Genuine Free Pascal compiler, 3.2.2. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
dcc32 hello.dpr; hello.exe (oppure FPC in modalità Delphi nel work locale)
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.dpr`: `f6580480e5910b62273a311a3f47fb5b897bf7ecb02c9d4e4ff326d7a7e2dba7`

Primary sources:

- https://docwiki.embarcadero.com/RADStudio/en/Programs_and_Units_(Delphi)
- https://www.freepascal.org/docs.html
