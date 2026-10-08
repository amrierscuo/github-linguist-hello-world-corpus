# 0472 — Nim: `.nimrod`

Ruolo: Nome storico del sorgente Nimrod, stesso sottoinsieme sintattico echo/let del programma Nim; loader contemporaneo può richiedere .nim.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#472 Nim/hello.nim.

Toolchain richiesta: Nim1.6.14 Ubuntu, backend C/GCC. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Copiare il sorgente in build/hello.nim; nim c -r build/hello.nim
```

Risultato atteso: Hello, World! seguito da newline; exit0.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.nimrod`: `46f0e4621c8b9d1c31674c7086f534c6a673f52a940dfbea1c9bc168f14a494f`

Fonti primarie:

- https://nim-lang.org/docs/tut1.html
