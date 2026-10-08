# #556 Procfile

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Validare ed eseguire un Procfile locale che avvia il processo greeting.

Foreman originale legge la dichiarazione greeting: ruby greeting.rb, avvia il processo locale e registra il saluto e la sua terminazione con exit0. Un launcher reloca soltanto il Ruby autentico nel PATH isolato. Nessun deploy Heroku è effettuato.

## Toolchain e riproduzione

Foreman0.90.0, Thor1.4.0, Ruby3.2.3

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
foreman check -f Procfile; foreman start -f Procfile
```

## Risultato atteso e stato

Procfile valido; processo greeting emette Hello, World! e termina0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://devcenter.heroku.com/articles/procfile
- https://github.com/ddollar/foreman
