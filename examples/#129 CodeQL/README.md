# #129 CodeQL

Voce canonica: `CodeQL`, tipo `programming`, `language_id: 424259634`.

Return one single line CodeQL with greeting column equal to Hello, World! by concatenation of strings.

## Toolchain and reproduction

Required native toolchain unavailable or not configured, unavailable version / not verified. Test environment: **Windows x64**.

It requires the authentic CodeQL CLI. qlpack.yml defines a local query pack without dependencies; the constant query does not matter a specific analysis scheme or libraries of a language. The evaluation command is to be checked with the available CLI; if it requires a database, use a compatible local test.

Comando/procedura from the example directory, except the build directory explicitly indicated:

```text
codeql query compile hello.ql; codeql query run hello.ql --output hello.bqrs; codeql bqrs decode --format=csv hello.bqrs
```

Expected result: Query compiled; table with a greeting column and a Hello, World! line.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Greeting is a value of select QL, not a comment. CLI has not been found and no results have been compiled or decoded. No remote repository, token or account is a requirement for local preparation of this example.

Remaining requirements:

- CodeQL native CLI is unavailable; query compile/evaluation remains pending and requires no external repository/account.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain versions and SHA-256 values for the artifacts. The `path_normalization` property documents
local route replacements. `<corpus>` identifies the relative files included in
final corpus, which were first verified in the staging directory.
sources remain those identified by checksums. The only offspring of availability
instruments do not attest parsing or execution.
in the work directory and are not included in the corpus.

## Primary sources

- [https://codeql.github.com/docs/ql-language-reference/queries/](https://codeql.github.com/docs/ql-language-reference/queries/)
- [https://docs.github.com/en/code-security/reference/code-scanning/codeql/codeql-cli-manual/query-compile](https://docs.github.com/en/code-security/reference/code-scanning/codeql/codeql-cli-manual/query-compile)
- [https://docs.github.com/en/code-security/reference/code-scanning/codeql/codeql-cli-manual/query-run](https://docs.github.com/en/code-security/reference/code-scanning/codeql/codeql-cli-manual/query-run)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ql` | [hello.ql](hello.ql), [consumer.ql](variants/ext-qll-2e716c6c/consumer.ql) created; verification pending |
| `.qll` | [hello.qll](variants/ext-qll-2e716c6c/hello.qll) created; verification pending |
