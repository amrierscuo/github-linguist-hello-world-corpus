# #825 nanorc

Caricare una nanorc locale e colorare il saluto nel buffer di prova.

## Toolchain

 GNU nano, version 7.2

## Procedura

nano --rcfile hello.nanorc greeting.hello; uscire senza salvataggio con Ctrl-X.

## Risultato atteso

Nano accetta la nanorc, mostra numeri di riga e colora Hello, World! in blu brillante.

## Stato

Sintassi e semantica verificate.

--rcfile evita configurazioni utente/globali. Il buffer e la regola highlight sono originali; la prova PTY deve confermare parsing e sequenze colore del testo.

Verifica reale 2026-10-08T13:50:49.777443+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://www.nano-editor.org/dist/latest/nanorc.5.html](https://www.nano-editor.org/dist/latest/nanorc.5.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.nanorc` | [hello.nanorc](hello.nanorc) verificato |
