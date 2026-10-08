# 0472 — Nim: `.nim.cfg`

Ruolo: Opzioni del compilatore Nim, non un programma Nim.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Nim1.6.14 Ubuntu, backend C/GCC. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
nim c --out:build/hello hello.nim; ./build/hello (Nim carica hello.nim.cfg associato)
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.nim`: `076562c4b011aa8f2efd2cbc2dc88d3afb525f4e5666e8e97ccbe7c94315c002`
- `hello.nim.cfg`: `06851203890f5cddb3ccafc38ddbe8b28c3bd825ec38fb5b8ce5725667ea0619`

Fonti primarie:

- https://nim-lang.org/docs/nimc.html#compiler-usage-configuration-files
- https://nim-lang.org/docs/tut1.html
