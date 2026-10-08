# #705 TXL

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Trasformare una sequenza di token in una stringa di saluto TXL.

Grammatica program come repeat token e funzione main di riscrittura; l’output stringlit rappresenta il saluto.

## Toolchain e riproduzione

TXL, versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
txl input.txt hello.txl
```

## Risultato atteso e stato

Token stringlit "Hello, World!" in output.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Interprete TXL non disponibile; parser e trasformazione pendenti.

## Fonti primarie

- https://www.txl.ca/plow2014.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.txl` | [hello.txl](hello.txl) creato, verifiche pendenti |
