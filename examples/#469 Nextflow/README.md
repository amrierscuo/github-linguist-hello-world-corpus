# #469 Nextflow

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Perform a local workflow Nextflow that produces Hello, World!.

The GREETING process emits stdout from its Bash task; workflow connects the channel to view. The source is a DSL2 pipeline, distinct from the script of the single task.

## Toolchain and reproduction

NextflowDSL2, Java21 e Bash; versioni effettive da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
nextflow run hello.nf
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Impedimenti: Runtime Nextflow e dipendenze Java non preparati; pipeline pendente.

## Primary sources

- https://nextflow.io/docs/latest/script.html
- https://nextflow.io/docs/latest/process.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.nf` | [hello.nf](hello.nf) created; verification pending |
