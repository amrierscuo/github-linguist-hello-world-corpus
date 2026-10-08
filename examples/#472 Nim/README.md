# #472 Nim

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Compilare Nim e stampare Hello, World!.

let lega una stringa, & concatena e echo effettua l’IO. Il compiler originale esegue parsing/typecheck e produce il programma C compilato da GCC; binario e cache restano in work.

## Toolchain e riproduzione

Nim1.6.14 Ubuntu, backend C/GCC

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
nim c --out:hello hello.nim
```

```text
./hello
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://nim-lang.org/docs/tut1.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.nim` | [hello.nim](hello.nim), [hello.nim](variants/nim-cfg-a023dc1f/hello.nim) creato, verifiche pendenti |
| `.nim.cfg` | [hello.nim.cfg](variants/nim-cfg-a023dc1f/hello.nim.cfg) creato, verifiche pendenti |
| `.nimble` | [hello.nimble](variants/nimble-ba115bce/hello.nimble) creato, verifiche pendenti |
| `.nimrod` | [hello.nimrod](variants/nimrod-b772c342/hello.nimrod) creato, verifiche pendenti |
| `.nims` | [hello.nims](variants/nims-27124d6b/hello.nims) creato, verifiche pendenti |
