# 0293 — Haskell: `.hs-boot`

Ruolo: Interfaccia hs-boot per una dipendenza SOURCE ciclica: solo firma, non main.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Hugs98 September2006, pacchetto98.200609.21-6build3 e librerie bundled Ubuntu. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
GHC: ghc --make Main.hs -o hello; ./hello
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `Audience.hs`: `906024b298648c82869a886f69b07ea87c1ebf2758e5f4b09d8402c51e03f844`
- `Greeting.hs`: `2c58ca0bf12a93c2bbedcff45ee04d8b93053c62b892e439783a2a1e089911e6`
- `Greeting.hs-boot`: `97ddd611f6354573607be4994915078c05a5276e4ba88008a3f442ed9f5e3cd3`
- `Main.hs`: `6314a6128930c6a895d4bee637b87a00a0c45505b97531ea2f1dce7059342f15`

Fonti primarie:

- https://downloads.haskell.org/ghc/latest/docs/users_guide/separate_compilation.html#mutually-recursive-modules-and-hs-boot-files
- https://www.haskell.org/hugs/
- https://www.haskell.org/onlinereport/haskell2010/haskellch9.html
