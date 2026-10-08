# #061 Bend

Voce canonica del `reference/languages.yml` del corpus. Il riferimento e il suo ordine restano invariati. Il sorgente è originale di questo esempio.

## Obiettivo

Stampare Hello, World! attraverso IO.print nel dialetto Bend 2.

Il compilatore originale Bend 2 è eseguito tramite Bun. Il backend JavaScript produce il programma poi eseguito da Node; il runtime effs del compilatore deve essere disponibile accanto all’output. Questa prova riguarda Bend 2, non il precedente runtime HVM.

## Toolchain e riproduzione

Bend 2.0.36; Bun 1.4.2; Node.js 22.20.0

Comandi dalla cartella dell’esempio, con la toolchain indicata disponibile nel PATH. Eseguire la build in una copia temporanea per mantenere fuori dal corpus i file generati.

```text
bend hello.bend --check-only
bend hello.bend -o hello.js
```

```text
node hello.js
```

## Risultato atteso e stato

stdout esatto: Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra comandi effettivi, versioni/provenienza della toolchain, codici di uscita, stdout/stderr e SHA-256 dei sorgenti provati. I percorsi della macchina sono normalizzati.

## Fonti primarie

- https://github.com/bendlang/bend
- https://github.com/bendlang/bend/blob/main/guide/GUIDE.md

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bend` | [hello.bend](hello.bend) verificato |
