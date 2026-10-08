# #622 Rocq Prover

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Definire il saluto e verificare una prova di uguaglianza, quindi valutarlo con Compute.

Elaborazione nativa e kernel Coq controllano greeting_value; Compute valuta la concatenazione. Coq8.18 è la versione effettivamente eseguita, non un runtime Rocq9.

## Toolchain e riproduzione

Coq8.18.0 originale (linguaggio oggi denominato Rocq Prover)

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
coqc hello.v
```

## Risultato atteso e stato

Compute produce "Hello, World!" : string e la prova compila.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://rocq-prover.org/doc/V8.19.2/refman/language/core/definitions.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.v` | [hello.v](hello.v) verificato |
| `.coq` | [hello.coq](variants/coq-98f35b68/hello.coq) creato, verifiche pendenti |
