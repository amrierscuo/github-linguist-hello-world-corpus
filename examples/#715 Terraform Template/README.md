# #715 Terraform Template

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Valutare un Terraform Template con audience = World.

templatefile interpreta realmente il file .tftpl e la variabile. La prova non usa provider, infrastruttura, init, stato remoto o rete.

## Toolchain e riproduzione

Terraform1.16.5 ufficiale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
terraform console < evaluate.txt
```

## Risultato atteso e stato

Valore stringa Hello, World! seguito da newline; console può usare notazione heredoc.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://developer.hashicorp.com/terraform/language/functions/templatefile

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.tftpl` | [hello.tftpl](hello.tftpl) verificato |
