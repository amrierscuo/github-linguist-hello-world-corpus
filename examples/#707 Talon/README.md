# #707 Talon

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Inserire Hello, World! quando Talon riconosce il comando hello world.

Il file dichiara un contesto globale e l’azione insert. L’esecuzione richiede Talon e una sessione di input controllata.

## Toolchain e riproduzione

Talon, versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
Talon: caricare hello.talon nel profilo di prova e pronunciare hello world
```

## Risultato atteso e stato

Testo inserito Hello, World!.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Talon non disponibile; riconoscimento e inserimento pendenti.

## Fonti primarie

- https://talonvoice.com/docs/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.talon` | [hello.talon](hello.talon) creato, verifiche pendenti |
