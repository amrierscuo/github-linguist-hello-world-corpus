# 0270 GraphQL: variant `.gql`

## Recorded verification

**Syntax and behavior verified** on November 4, 2026. Load variant query with corpus schema, and variant schema with an independent query; run GraphQL.js with World, Reader, null and the schema default. [Evidence](../../verification/native_20261104_270_variants_result.json).

Role: Textual Alias of the same format and of the same programma/dataset of the original model.

Tipo variante: **alias**. Copia byte-identica di examples/#270 GraphQL/hello.graphql

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
GraphQL parser: parse hello.gql; eseguire sullo schema originale con variabile name=World e resolver greeting.
```

Expected result: greeting= Hello, World!; correct Reader control and null input; PASS.

## Earlier status
Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://www.graphql-js.org/docs/](https://www.graphql-js.org/docs/)
- [https://github.com/graphql/graphql-js](https://github.com/graphql/graphql-js)
- [https://spec.graphql.org/](https://spec.graphql.org/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
