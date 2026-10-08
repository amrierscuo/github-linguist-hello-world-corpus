# 0522 — POV-Ray SDL: `.inc`

Ruolo: Include POV-Ray che definisce un oggetto text TrueType; scena driver separata.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Original POV-Ray SDL parser and renderer — POV-Ray 3.7.0.10 Ubuntu 3build4. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
povray +Idriver.pov +Ohello.png +W800 +H200 -D
```

Risultato atteso: Testo Hello, World! nel render

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `driver.pov`: `5054100ed69fc2682049fba08a75945c831dbf0f51c596c5eb4c94cfeccfcf2b`
- `hello.inc`: `99a22007af1b9872a88f222929edfb64825787bd4f3ef9c25003fb516a5f6046`

Fonti primarie:

- https://www.povray.org/documentation/view/3.7.0/290/
- https://www.povray.org/documentation/
