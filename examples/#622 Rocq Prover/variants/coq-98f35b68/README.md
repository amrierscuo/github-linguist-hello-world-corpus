# 0622: Rocq Prover: `.coq`

Textual variation of the same format, with canon suffix .coq.

Origin: copy of the original `examples/#622 Rocq Prover/hello.v` file.

Artefatto principale: `hello.coq`.

Control provided, from the folder of the variant:

```text
coqc -o work/hello.vo hello.coq
```

Expected result: Compute produces "Hello, World!": string and test compile..

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://rocq-prover.org/doc/V8.19.2/refman/language/core/definitions.html](https://rocq-prover.org/doc/V8.19.2/refman/language/core/definitions.html)
