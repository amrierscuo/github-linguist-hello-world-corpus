# #792 Xmake

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Interpretare xmake.lua, compilare la fixture C ed eseguire Hello, World!.

Xmake interpreta target, set_kind e add_files e invoca GCC. Cache/configurazione e build della prova sono isolate in work.

## Toolchain e riproduzione

Xmake3.1.1+HEAD.3ba37a0 bundle originale e GCC Ubuntu

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
xmake f -y -p linux --toolchain=gcc -o build; xmake -y; ./build/linux/x86_64/release/hello
```

## Risultato atteso e stato

Build exit0 e programma compilato stampa Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://xmake.io/guide/quick-start.html
