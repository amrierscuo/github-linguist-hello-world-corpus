# 0634: SPARQL: `.sparql`

## Latest recorded verification

**Syntax and behavior verified** for `.sparql`. RDFlib SPARQL parser and query evaluator: one greeting binding. [Recorded evidence](../../verification/native_20261104_followup_2e73706172716c.json).

Textual variation of the same format, with canon suffix .sparql.

Origin: copy of the original `examples/#634 SPARQL/hello.rq` file.

Artefatto principale: `hello.sparql`.

Control provided, from the folder of the variant:

```text
rdflib SPARQL engine: execute hello.sparql and assert the greeting binding
```

Expected result: One line with greeting = Hello, World!..

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.w3.org/TR/sparql11-query/#func-concat](https://www.w3.org/TR/sparql11-query/#func-concat)
