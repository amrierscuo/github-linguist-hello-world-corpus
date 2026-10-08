# #383 LigoLANG

Valutare una costante stringa del saluto nella sintassi PascaLIGO della baseline .ligo.

## Toolchain

LIGO compatibile con PascaLIGO, ad esempio serie 0.73; versione effettiva da registrare

## Comandi e procedura

Con un compilatore che supporta PascaLIGO: ligo run evaluate-expr hello.ligo greeting --syntax pascaligo --deprecated

## Risultato atteso

Il valore di greeting è la stringa Hello, World!.

## Stato

Sintassi e semantica in attesa.

L’estensione canonica .ligo identifica PascaLIGO storico. Il file non viene rinominato come JsLIGO: i compilatori recenti richiedono un percorso di migrazione. La versione compatibile e l’opzione deprecata vanno provate prima di dichiarare valutazione positiva.

Requisiti residui:
- Compilatore con supporto PascaLIGO non disponibile; sintassi/evaluation pending.

## Fonti primarie

- [https://gitlab.com/ligolang/ligo](https://gitlab.com/ligolang/ligo)
- [https://ligolang.org/docs/next/intro/changelog/](https://ligolang.org/docs/next/intro/changelog/)
- [https://gitlab.com/ligolang/ligo/-/merge_requests/2395](https://gitlab.com/ligolang/ligo/-/merge_requests/2395)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ligo` | [hello.ligo](hello.ligo) creato, verifiche pendenti |
