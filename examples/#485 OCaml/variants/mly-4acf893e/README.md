# 0485: OCaml: `.mly`

Role: Grammar ocamlyacc with token HELLO and function that returns greeting.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: OCaml 4.14.1. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
ocamlyacc hello.mly; ocamlc -c hello.mli; ocamlc -c hello.ml; ocamlc -o driver hello.cmo driver.ml; ./driver
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `driver.ml`: `e6f6c8a85d4d80140be528bd622b6db2b0c82d9aa5079aedf2b10c63b2bf95f7`
- `hello.mly`: `997a0f330e10d8004df0b38df1fcbb1616fedabfcd089dfa3bfafa993f1e465e`

Primary sources:

- https://ocaml.org/manual/5.3/lexyacc.html
- https://ocaml.org/manual/5.4/programs.html
