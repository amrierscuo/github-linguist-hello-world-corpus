# 0129 CodeQL: variant `.qll`

Role: CodeQL .qll Library exports a function, imported from the companion query.

Type: **adapted**. Starting model: examples/#129 CodeQL/hello.ql; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
codeql query compile consumer.ql; codeql query run consumer.ql --database=<database-C-piccolo-esterno>
```

Expected result: Hello, World!

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://codeql.github.com/docs/ql-language-reference/queries/](https://codeql.github.com/docs/ql-language-reference/queries/)
- [https://docs.github.com/en/code-security/reference/code-scanning/codeql/codeql-cli-manual/query-compile](https://docs.github.com/en/code-security/reference/code-scanning/codeql/codeql-cli-manual/query-compile)
- [https://docs.github.com/en/code-security/reference/code-scanning/codeql/codeql-cli-manual/query-run](https://docs.github.com/en/code-security/reference/code-scanning/codeql/codeql-cli-manual/query-run)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://codeql.github.com/docs/ql-language-reference/modules/](https://codeql.github.com/docs/ql-language-reference/modules/)
