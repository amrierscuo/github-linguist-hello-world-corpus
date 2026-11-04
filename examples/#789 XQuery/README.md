# #789 XQuery

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Valutare XQuery3.1 e restituire Hello, World!.

Saxon analyzes and evaluates the variabile/concat. On Windows use; as a classpath separator instead of:.

## Toolchain and reproduction

Saxon-HE12.9 originale e XML Resolver5.3.3, OpenJDK21

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
java -cp "saxon-he.jar:xmlresolver.jar" net.sf.saxon.Query -q:hello.xq "!method=text"
```

## Expected result and status

Hello, World! serialized as text.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.w3.org/TR/xquery-31/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.xquery` | [hello.xquery](variants/xquery-d1e42ae2/hello.xquery) syntax and behavior verified |
| `.xq` | [hello.xq](hello.xq), [main.xq](variants/xqm-6120106c/main.xq) syntax and behavior verified |
| `.xql` | [hello.xql](variants/xql-598d9a0b/hello.xql) syntax and behavior verified |
| `.xqm` | [hello.xqm](variants/xqm-6120106c/hello.xqm) syntax and behavior verified |
| `.xqy` | [hello.xqy](variants/xqy-27e37189/hello.xqy) syntax and behavior verified |

## Additional extension verification

- `.xquery`: verified on November 4, 2026. [Evidence](verification/native_20261104_789_variants_result.json).
- `.xq`: verified on November 4, 2026. [Evidence](verification/native_20261104_789_variants_result.json).
- `.xql`: verified on November 4, 2026. [Evidence](verification/native_20261104_789_variants_result.json).
- `.xqm`: verified on November 4, 2026. [Evidence](verification/native_20261104_789_variants_result.json).
- `.xqy`: verified on November 4, 2026. [Evidence](verification/native_20261104_789_variants_result.json).
