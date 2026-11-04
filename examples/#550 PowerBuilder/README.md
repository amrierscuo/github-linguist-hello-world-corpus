# #550 PowerBuilder

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Import a PowerBuilder user object and show Hello, World! by calling us greet.

The exported source .sru defines a non-visual object and a public function PowerScript. MessageBox sends greeting; the return value is0.

## Toolchain and reproduction

Appeon PowerBuilder originale; versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
Importare u_hello.sru in una libreria PowerBuilder; istanziare u_hello e chiamare greet().
```

## Expected result and status

MessageBox shows Hello, World!.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Impedimenti: Ambiente PowerBuilder non preparato; import/compilazione/esecuzione pendenti.

## Primary sources

- https://www.appeon.com/system/files/product-manual/powerscript_reference_v2021.pdf

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pbt` | [hello.pbt](variants/pbt-c9751eff/hello.pbt) created; verification pending |
| `.sra` | [corpus_hello.sra](variants/sra-88988218/corpus_hello.sra) created; verification pending |
| `.sru` | [u_hello.sru](u_hello.sru) created; verification pending |
| `.srw` | [w_hello.srw](variants/srw-92c044a7/w_hello.srw) created; verification pending |
