# 0485: OCaml: `.mli`

Ruolo: Interfaccia OCaml dichiarativa: val greeting, implementazione e main separati.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: OCaml 4.14.1. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
ocamlc -c greeting.mli; ocamlc -c greeting.ml; ocamlc -o hello greeting.cmo main.ml; ./hello
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `greeting.ml`: `9f86810393a29016ca792ebe4513e9693808a6d66980cd4dc18a88b9abab1f94`
- `greeting.mli`: `3540feaa3df9e3613e5afe11b348a90f7b42e21978d8303a29075cfa14e12b9a`
- `main.ml`: `70213b9bc2df66f4f978734722cac6abf3e7865a5f72422b78ce310e09745724`

Primary sources:

- https://ocaml.org/manual/5.3/moduleexamples.html
- https://ocaml.org/manual/5.4/programs.html
