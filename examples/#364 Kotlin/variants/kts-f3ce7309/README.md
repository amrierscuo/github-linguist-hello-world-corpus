# 0364 — Kotlin: `.kts`

Ruolo: Script Kotlin con istruzioni top-level; non funzione main non invocata.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Kotlin2.4.21, OpenJDK21 Microsoft. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
kotlinc -script hello.kts
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.kts`: `f80efc3925d937e1d8b2cacbfbd6f830a2778b5ca4ff31f2caa8782723861c95`

Fonti primarie:

- https://kotlinlang.org/docs/command-line.html
- https://github.com/JetBrains/kotlin/releases/tag/v2.4.21
