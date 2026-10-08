# #361 Kit

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Renderizzare un template Kit con variabile audience e ottenere il paragrafo Hello, World!.

Le direttive sono commenti speciali Kit: assegnazione $audience e sostituzione della variabile. Il saluto non dipende da commenti ordinari ignorati da HTML.

## Toolchain e riproduzione

CodeKit con compiler Kit originale; versione da registrare

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
Compilare hello.kit con CodeKit/Kit.
```

## Risultato atteso e stato

HTML contiene <p>Hello, World!</p>.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compilatore/runtime nativo eseguito per questa voce.

Impedimenti: Compiler originale Kit scritto per Cocoa/macOS non disponibile; renderer non eseguito.

## Fonti primarie

- https://codekitapp.com/help/kit/index.html
- https://github.com/bdkjones/Kit

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.kit` | [hello.kit](hello.kit) creato, verifiche pendenti |
