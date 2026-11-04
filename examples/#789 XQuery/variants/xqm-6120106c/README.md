# 0789: XQuery: `.xqm`

## Recorded verification

**Syntax and behavior verified** on November 4, 2026. Saxon processes three standalone XQuery suffixes plus the original main.xq importer and hello.xqm library. Aggregate .xq keeps the prior unchanged main example proof. [Evidence](../../verification/native_20261104_789_variants_result.json).

Library module XQuery with namespace and function, distinct from the main query.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.xqm`.

Control provided, from the folder of the variant:

```text
basex main.xq
```

Expected result: Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.w3.org/TR/xquery-31/#id-module-imports](https://www.w3.org/TR/xquery-31/#id-module-imports)
