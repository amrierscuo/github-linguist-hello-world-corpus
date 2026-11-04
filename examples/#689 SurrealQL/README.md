# #689 SurrealQL

Voce canonica `SurrealQL`, tipo `programming`, language_id `735141027`.

Evaluate a RETURN SurrealQL with string concatenation.

## Toolchain and reproduction

Required genuine surreal compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires SurrealDB CLI/engine original with endpoint memory compatible.

Comando/procedura from the directory of the example, unless explicit indications:

```text
surreal sql --endpoint memory --namespace corpus --database greeting < hello.surql
```

Expected result: Hello, World! in the conformed result, according to the framework described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Original Query, local and without persistent records; unconfigured engine.

Remaining requirements:

- Required surreal toolchain and matching execution/format resources are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://surrealdb.com/docs/surrealql/statements/return](https://surrealdb.com/docs/surrealql/statements/return)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.surql` | [hello.surql](hello.surql) created; verification pending |
