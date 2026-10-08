# #660 Sieve

Filtrare offline un messaggio Sieve in base al saluto nel Subject.

## Toolchain

Sieve compiler/test engine

## Procedura

sievec hello.sieve; sieve-test hello.sieve hello.eml; verificare fileinto INBOX.CorpusGreeting.

## Risultato atteso

Per il fixture Subject=Hello, World! il risultato è fileinto INBOX.CorpusGreeting.

## Stato

Sintassi e semantica in attesa.

Messaggio originale con indirizzi example.invalid; verifica prevista offline, senza spedizioni.

Requisiti residui:
- Sieve compiler/offline test engine non disponibile.

## Fonti primarie

- [https://www.rfc-editor.org/rfc/rfc5228](https://www.rfc-editor.org/rfc/rfc5228)
- [https://doc.dovecot.org/2.3/configuration_manual/sieve/](https://doc.dovecot.org/2.3/configuration_manual/sieve/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sieve` | [hello.sieve](hello.sieve) creato, verifiche pendenti |
