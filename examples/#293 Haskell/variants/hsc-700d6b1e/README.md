# 0293 — Haskell: `.hsc`

Ruolo: Sorgente hsc2hs: preprocessamento include C, poi normale programma Haskell.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Hugs98 September2006, pacchetto98.200609.21-6build3 e librerie bundled Ubuntu. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
hsc2hs hello.hsc -o Main.hs; ghc Main.hs -o hello; ./hello
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.hsc`: `06ea4d8ec1cf1da2f3deade5a82f24cdffd8d7d095cc8180e805159e0d865e8c`

Fonti primarie:

- https://downloads.haskell.org/ghc/latest/docs/users_guide/utils.html#hsc2hs
- https://www.haskell.org/hugs/
- https://www.haskell.org/onlinereport/haskell2010/haskellch9.html
