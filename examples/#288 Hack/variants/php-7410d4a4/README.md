# 0288 — Hack: `.php`

Ruolo: Sorgente Hack con tag <?hh e entry point HHVM; non è un programma PHP.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: HHVM/Hack e typechecker hh_client; versioni effettive da registrare. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
hh_client; hhvm hello.php
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.php`: `f0d3a9127b2b5314d4505c825137f6aa22e3e95e47aa32098a8d2af349498045`

Fonti primarie:

- https://docs.hhvm.com/hack/getting-started/getting-started
- https://docs.hhvm.com/hack/source-code-fundamentals/program-structure/
- https://hacklang.org/
