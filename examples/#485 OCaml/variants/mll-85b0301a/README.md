# 0485: OCaml: `.mll`

Role: Specify ocamllex with rule that recognizes greeting; includes trailer main.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: OCaml 4.14.1. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
ocamllex hello.mll; ocamlc -o hello hello.ml; ./hello
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.mll`: `b451bfd0e67cb81b0a713116e68403f1099cce7cb0990c3b2a2d1ec7d07feac3`

Primary sources:

- https://ocaml.org/manual/5.3/lexyacc.html
- https://ocaml.org/manual/5.4/programs.html
