# #165 Dhall

Valutare un valore Text Dhall interpolato e ottenere Hello, World! senza newline.

## Toolchain

Dhall 1.42.2

## Comandi e procedura

dhall version; dhall type --file hello.dhall; dhall text --file hello.dhall

## Risultato atteso

Tipo Text; export text restituisce esattamente Hello, World!, exit 0.

## Stato

Sintassi e semantica verificate.

Il type checker e il normalizzatore ufficiali risolvono target : Text e interpolazione. La sorgente non importa risorse di rete.

Verifica effettiva del 2026-10-08T11:56:10.980886+00:00 su Windows x64: [log](verification/result.json).
Hash delle sorgenti/checker, versioni e comandi reali, codici di uscita, stdout/stderr e limiti della prova sono nel log.

## Fonti primarie e riferimento di formato

- [https://docs.dhall-lang.org/tutorials/Getting-started_Generate-JSON-or-YAML.html](https://docs.dhall-lang.org/tutorials/Getting-started_Generate-JSON-or-YAML.html)
- [https://github.com/dhall-lang/dhall-haskell/releases/tag/1.42.2](https://github.com/dhall-lang/dhall-haskell/releases/tag/1.42.2)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.dhall` | [hello.dhall](hello.dhall) verificato |
