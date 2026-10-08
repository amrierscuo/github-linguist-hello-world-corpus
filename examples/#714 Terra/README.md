# #714 Terra

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Compilare JIT una funzione Terra e stampare Hello, World!.

Il programma Lua ospitante dichiara una funzione terra, importa stdio e la invoca; Lua senza Terra non esegue questo linguaggio.

## Toolchain e riproduzione

Terra con LLVM/Clang, versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
terra hello.t
```

## Risultato atteso e stato

Hello, World! su stdout.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Terra runtime non predisposto; verifica JIT e chiamata C pendenti.

## Fonti primarie

- https://terralang.org/getting-started.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.t` | [hello.t](hello.t) creato, verifiche pendenti |
