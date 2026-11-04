# #547 PostCSS

## Latest recorded verification

Latest extension checks:
- `.postcss`: PostCSS and the custom properties plugin transform this source and verify the greeting in the CSS content declaration. [Evidence](verification/native_20261104_followup_2e706f7374637373.json).

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Analyze PostCSS and solve a custom property in the content= Hello, World! value.

The .pcss source defines --greeting and uses it in content. The original parser and plugin transform the CSS; the driver reads the content value of the resulting AST. The test checks the transformation, without attributing a rendering browser.

## Toolchain and reproduction

PostCSS8 and postcss-custom-properties original; actual versions in the log

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
node verify.js
```

## Expected result and status

CSS transformer contains content: "Hello, World!".

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://postcss.org/
- https://github.com/csstools/postcss-plugins/tree/main/plugins/postcss-custom-properties

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pcss` | [hello.pcss](hello.pcss) verified |
| `.postcss` | [hello.postcss](variants/postcss-ca8f3f2b/hello.postcss) syntax and behavior verified |