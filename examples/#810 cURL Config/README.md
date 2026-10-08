# #810 cURL Config

Leggere .curlrc e consumare il saluto del header via HTTP loopback.

## Toolchain

curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP; CPython3.13.9

## Procedura

python verify.py <curl-executable>

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

La risposta del server deriva dal header ricevuto: prova effettiva delle opzioni di configurazione. Porta effimera loopback, nessuna richiesta esterna.

Verifica reale 2026-10-08T13:38:35.028326+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://curl.se/docs/manpage.html#-K](https://curl.se/docs/manpage.html#-K)
