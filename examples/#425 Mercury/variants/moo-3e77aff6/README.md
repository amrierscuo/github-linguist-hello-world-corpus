# 0425: Mercury: `.moo`

Role: Original Grammar Moose, not ordinary Mercury program: recognizes the hello token and returns a string attribute with greeting.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Mercury mmc e grade runtime installata. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Moose originale: moose hello.moo > hello.m; poi compilare il modulo generato con mmc. Per una prova semantica, implementare parser_state con stream [hello,eof] e invocare il parse generato.
```

Expected result: The generator produces Mercury with parse_result greeting("Hello, World!") for hello,eof tokens; pendant execution.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.
- The grammar is documented; the execution of the generator and the parser_state driver is lacking, so both flags remain false.

SHA-256 of variant files:

- `hello.moo`: `a8ff8e11682f83328cb82f3241093992df3f7571ab1abef29373ab8194732d5d`

Primary sources:

- https://raw.githubusercontent.com/Mercury-Language/mercury/master/extras/moose/README
- https://raw.githubusercontent.com/Mercury-Language/mercury/master/extras/moose/samples/expr.moo
- https://www.mercurylang.org/information/doc-latest/mercury_user_guide/Hello-world.html
