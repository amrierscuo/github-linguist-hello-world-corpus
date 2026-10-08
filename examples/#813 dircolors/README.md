# #813 dircolors

Applicare dircolors e colorare il nome del fixture del saluto.

## Toolchain

dircolors (GNU coreutils) 9.4

## Procedura

TERM=xterm; eval "$(dircolors -b hello.dircolors)"; ls --color=always -- "Hello, World!.hello"

## Risultato atteso

Il nome Hello, World!.hello è preceduto dal codice ANSI bold-blue 01;34.

## Stato

Sintassi e semantica verificate.

dircolors genera realmente LS_COLORS e ls consuma il codice per .hello. EXEC 00 disabilita il colore degli eseguibili per rendere riproducibile la prova anche su filesystem Windows montati in WSL.

Verifica reale 2026-10-08T13:39:24.271672+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://www.gnu.org/software/coreutils/manual/html_node/dircolors-invocation.html](https://www.gnu.org/software/coreutils/manual/html_node/dircolors-invocation.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.dircolors` | [hello.dircolors](hello.dircolors) verificato |
