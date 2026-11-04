# 0485: OCaml: `.ml4`

Role: Standard OCaml Source as the text input of the Camlp4 preprocessor; it does not introduce undocumented grammar extensions.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: OCaml 4.14.1. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
In una directory di lavoro: camlp4o hello.ml4 > hello.ml; ocaml hello.ml
```

Expected result: Hello, World! and LF after Camlp4 preprocession and OCaml interpretation.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.
- Camlp4 original compatible unprepared. No evidence is inherited from the main OCaml.

SHA-256 of variant files:

- `hello.ml4`: `c299624d78a2d8dbde0f49b30bc937b30531ddf5d6e7684eb554a5b4fe51b7d1`

Primary sources:

- https://github.com/ocaml/camlp4
- https://caml.inria.fr/pub/old_caml_site/camlp4/tutorial/tutorial003.html
- https://ocaml.org/manual/5.4/programs.html
