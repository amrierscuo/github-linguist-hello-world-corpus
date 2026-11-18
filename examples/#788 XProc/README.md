# #788 XProc

## Verified on November 18, 2026

The official XProc processor executed the original identity step and serialized the expected greeting element.

Run `java -jar xmlcalabash-app-3.1.0.jar hello.xpl`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Perform an XProc3 pipeline that produces a greeting document.

La pipeline identity usa un input inline originale e porta result. Un parser XML generico non verifica il linguaggio di pipeline.

## Toolchain and reproduction

Processor XProc3 as XML Calabash3, version to be recorded

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
xmlcalabash hello.xpl
```

## Expected result and status

Documento <greeting>Hello, World!</greeting>.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Impedimenti: Processore XProc3 non predisposto; validazione e pipeline pendenti.

## Primary sources

- https://spec.xproc.org/3.0/xproc/xproc_letter.pdf

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.xpl` | [hello.xpl](hello.xpl) Syntax and behavior verified |
| `.xproc` | [hello.xproc](variants/xproc-8b475bd1/hello.xproc) created; verification pending |

</details>
