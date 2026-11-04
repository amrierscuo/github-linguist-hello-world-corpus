# #467 NetLogo

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Perform the greet procedure of a NetLogo model and print Hello, World!.

La procedura usa word e print; le sezioni .nlogo includono codice, info, versione e un esperimento BehaviorSpace originale. L’obiettivo è l’output della procedura, non il testo informativo del modello.

## Toolchain and reproduction

NetLogo6.4.0 or compatible version; not prepared

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
Aprire hello.nlogo in NetLogo e invocare greet.
```

## Expected result and status

Model console contains Hello, World!.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Impedimenti: Loader/compiler/runtime NetLogo non preparati; modello non aperto.

## Primary sources

- https://docs.netlogo.org/dict/print.html
- https://raw.githubusercontent.com/NetLogo/models/6.4.0/Sample%20Models/Biology/Wolf%20Sheep%20Predation.nlogo

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.nlogo` | [hello.nlogo](hello.nlogo) created; verification pending |
