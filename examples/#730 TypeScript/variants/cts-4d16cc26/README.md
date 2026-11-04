# 0730: TypeScript: `.cts`

## Recorded verification

**Syntax and behavior verified** on November 4, 2026. Compile both originals using strict NodeNext TypeScript settings and execute emitted .cjs and .mjs using Node. [Evidence](../../verification/native_20261104_730_variants_result.json).

TypeScript CommonJS module determined by the suffix.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.cts`.

Control provided, from the folder of the variant:

```text
tsc --target ES2022 --module NodeNext --moduleResolution NodeNext --outDir work hello.cts; node work/hello.cjs
```

Expected result: Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.typescriptlang.org/docs/handbook/modules/reference.html#module-format-detection](https://www.typescriptlang.org/docs/handbook/modules/reference.html#module-format-detection)
