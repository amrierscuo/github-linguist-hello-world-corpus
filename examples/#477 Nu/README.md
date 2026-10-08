# #477 Nu

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Interpretare Nu e stampare Hello, World!.

La forma puts è il builtin del linguaggio Nu. Il file .nu viene tenuto distinto da Nushell, che condivide l’estensione.

## Toolchain e riproduzione

Nu/nush originale con runtime Objective-C/Foundation; versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
nush hello.nu
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Nu/Objective-C Foundation non preparati; runtime pendente.

## Fonti primarie

- https://github.com/programming-nu/nu

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.nu` | [hello.nu](hello.nu) creato, verifiche pendenti |
