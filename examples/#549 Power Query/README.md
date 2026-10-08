# #549 Power Query

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Valutare un’espressione PowerQuery M e ottenere Hello, World!.

let lega Audience e Greeting; & concatena stringhe e in restituisce il valore. Il programma è M, distinto da PowerShell.

## Toolchain e riproduzione

PowerQuery M engine originale; versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
Caricare hello.pq in una query vuota PowerQuery e valutare.
```

## Risultato atteso e stato

Risultato stringa Hello, World!.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Engine PowerQuery non preparato; parsing/evaluation pendenti.

## Fonti primarie

- https://learn.microsoft.com/en-us/powerquery-m/m-spec-introduction
- https://learn.microsoft.com/en-us/powerquery-m/m-spec-consolidated-grammar

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pq` | [hello.pq](hello.pq) creato, verifiche pendenti |
