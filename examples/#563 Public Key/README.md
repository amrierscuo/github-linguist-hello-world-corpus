# #563 Public Key

Leggere una chiave pubblica dimostrativa Ed25519 con commento del saluto.

## Toolchain

OpenSSH_9.6p1 Ubuntu-3ubuntu13.19, OpenSSL 3.0.13 30 Jan 2024

## Procedura

ssh-keygen -t ed25519 -N "" -C "Hello, World!" -f <work-private-key>; ssh-keygen -lf hello.pub

## Risultato atteso

ssh-keygen riconosce ED25519 e mostra il commento Hello, World!.

## Stato

Sintassi e semantica verificate.

hello.pub è generata realmente per questo esempio. Il corpus contiene soltanto la chiave pubblica; la chiave privata temporanea resta in work. Il goal è la chiave valida e il commento, non cifrare il saluto.

Verifica reale 2026-10-08T13:16:51.649710+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://man.openbsd.org/ssh-keygen](https://man.openbsd.org/ssh-keygen)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.asc` | [hello.asc](variants/asc-431e050a/hello.asc) verificato |
| `.pub` | [hello.pub](hello.pub) verificato |
