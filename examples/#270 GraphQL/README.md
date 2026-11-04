# #270 GraphQL

Voce canonica `GraphQL`, tipo `data`, language_id `139`.

Analyze schema/query GraphQL, check the types and execute a parametric query with a local resolver.

## Toolchain and reproduction

Official GraphQL.js reference implementation, 16.11.0; Node.js 22.20.0. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

GraphQL.js official 16.11.0 and Node.js 22.20.0. No server/account is necessary; schema.graphql and hello.graphql files are original.

Comando/procedura from the directory of the example, unless explicit indications:

```text
npm install --prefix .tools graphql@16.11.0; node verify.cjs .tools
```

Expected result: greeting= Hello, World!; correct Reader control and null input; PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The valid AST test against schema, runs World and Reader and checks the error by name=null. The local resolver calculates the string through the authentic GraphQL execution engine.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.graphql-js.org/docs/](https://www.graphql-js.org/docs/)
- [https://github.com/graphql/graphql-js](https://github.com/graphql/graphql-js)
- [https://spec.graphql.org/](https://spec.graphql.org/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.graphql` | [hello.graphql](hello.graphql), [schema.graphql](schema.graphql) verified |
| `.gql` | [hello.gql](variants/ext-gql-2e67716c/hello.gql) syntax and behavior verified |
| `.graphqls` | [hello.graphqls](variants/ext-graphqls-2e6772617068716c73/hello.graphqls) syntax and behavior verified |

## Additional extension verification

- `.gql`: verified on November 4, 2026. [Evidence](verification/native_20261104_270_variants_result.json).
- `.graphqls`: verified on November 4, 2026. [Evidence](verification/native_20261104_270_variants_result.json).
