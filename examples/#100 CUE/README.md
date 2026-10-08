# #100 CUE

Costruire il saluto da prefix e target con interpolazione CUE, unificarlo con il vincolo Hello, World! ed esportare il valore testo.

## Toolchain

cue version v0.17.1

## Comandi e procedura

Con il binario ufficiale CUE v0.17.1:

```sh
cue version
cue vet hello.cue
cue export hello.cue -e greeting --out text
```

prefix e target costruiscono il valore interpolato; la seconda dichiarazione
di greeting lo vincola al saluto atteso. Un valore incompatibile farebbe
fallire la valutazione. Il formato text esporta soltanto il saluto.

## Risultato atteso

cue vet exit 0; export exit 0, stdout Hello, World! seguito da newline.

## Stato

Sintassi e semantica verificate.

Le due dichiarazioni greeting sono vincoli che CUE unifica, non un override. L'evaluatore reale verifica interpolazione e compatibilità del saluto finale.

Verifica effettiva del 2026-10-08T11:33:52.311212+00:00 su Windows x64: [log](verification/result.json).
Il log include hash SHA-256 della sorgente e dei checker, versioni, comandi, codici di uscita, stdout, stderr e limiti della prova.

## Fonti primarie

- [https://cuelang.org/docs/reference/spec/](https://cuelang.org/docs/reference/spec/)
- [https://cuelang.org/docs/cmd/cue/export/](https://cuelang.org/docs/cmd/cue/export/)
- [https://github.com/cue-lang/cue/releases/tag/v0.17.1](https://github.com/cue-lang/cue/releases/tag/v0.17.1)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cue` | [hello.cue](hello.cue) verificato |
