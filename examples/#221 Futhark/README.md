# #221 Futhark

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Compilare Futhark ed ottenere i 13 byte UTF-8 di Hello, World! dall’entry point main.

Futhark è un linguaggio puro: le stringhe sono array u8. main concatena due stringhe e il programma CLI generato restituisce l’array numerico. La verifica confronta tutti i byte dell’output con il saluto; il runtime non offre una stampa testuale nel sorgente.

## Toolchain e riproduzione

Futhark 0.27.1, GHC 9.10.3 build ufficiale; GNU C 13.3.0 in WSL

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
futhark check hello.fut
futhark c hello.fut -o hello
```

```text
./hello
```

## Risultato atteso e stato

[72u8, 101u8, 108u8, 108u8, 111u8, 44u8, 32u8, 87u8, 111u8, 114u8, 108u8, 100u8, 33u8]

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://futhark.readthedocs.io/en/latest/language-reference.html
- https://futhark.readthedocs.io/en/latest/usage.html
- https://github.com/diku-dk/futhark/releases/tag/v0.27.1

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.fut` | [hello.fut](hello.fut) verificato |
