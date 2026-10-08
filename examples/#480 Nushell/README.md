# #480 Nushell

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Interpretare Nushell e stampare Hello, World!.

let lega audience e la stringa interpolata $"..." usa ($audience). L’esecutore originale viene avviato senza caricare la configurazione personale.

## Toolchain e riproduzione

Nushell0.116.1 ufficiale Windows

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
nu --no-config-file hello.nu
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.nushell.sh/book/scripts.html
- https://github.com/nushell/nushell/releases/tag/0.116.1

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.nu` | [hello.nu](hello.nu) verificato |
