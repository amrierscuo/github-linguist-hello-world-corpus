# #639 SSH Config

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Analizzare SSH Config e valutare l’opzione GREETING=Hello, World!.

-G stampa la configurazione effettiva senza aprire connessioni. Il file rimane una fixture locale; il nome host illustrativo usa example.invalid.

## Toolchain e riproduzione

OpenSSH9.6p1 originale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
ssh -G -F ssh-config hello-world
```

## Risultato atteso e stato

hostname hello-world.example.invalid e setenv GREETING=Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://man.openbsd.org/ssh_config
