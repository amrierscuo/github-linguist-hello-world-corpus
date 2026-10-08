# 0384 — LilyPond: `.ily`

Ruolo: Include LilyPond con markup del saluto; driver separato lo include.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: LilyPond 2.24 compatibile; versione effettiva da registrare. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
lilypond driver.ly
```

Risultato atteso: Testo Hello, World! nel rendering PDF/SVG

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `driver.ly`: `9b7b92a752134d5e08f55976a8ebab2b85d7331992984095ec8dbe9eba02f34f`
- `hello.ily`: `81e9dd825021b2137b18e7e0029c998a4f8041054f24e852ea16ff2964d4de24`

Fonti primarie:

- https://lilypond.org/doc/v2.24/Documentation/notation/including-lilypond-files
- https://lilypond.org/doc/v2.24/Documentation/learning/
- https://lilypond.org/doc/v2.24/Documentation/usage/command_002dline-usage
