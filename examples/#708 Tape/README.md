# #708 Tape

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Descrivere una registrazione terminale con echo Hello, World! nel linguaggio Tape di VHS.

Tape .tape è il linguaggio di registrazione di VHS nella voce canonica. Il parser originale valida il file senza avviare una registrazione.

## Toolchain e riproduzione

VHS0.12.1 originale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
vhs validate hello.tape; vhs hello.tape
```

## Risultato atteso e stato

Tape valido; registrazione attesa mostra il comando e Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: no.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

Impedimenti: Registrazione/controllo del video non eseguiti; richiede ttyd, ffmpeg e browser compatibile.

## Fonti primarie

- https://github.com/charmbracelet/vhs

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.tape` | [hello.tape](hello.tape) sintassi verificata |
