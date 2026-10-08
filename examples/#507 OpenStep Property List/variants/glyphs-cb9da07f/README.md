# 0507 — OpenStep Property List: `.glyphs`

Ruolo: Dati del linguaggio canonico OpenStep Property List; schema progetto Glyphs e font completo non verificati.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Python 3.13.9 + openstep-parser 2.0.3. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Parser originale di OpenStep Property List: leggere hello.glyphs
```

Risultato atteso: Dizionario OpenStep con greeting Hello, World!; nessuna promessa di font Glyphs valido.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.
- Lo schema progetto/font Glyphs resta non verificato; non importare il fixture come font completo.

SHA-256 dei file della variante:

- `hello.glyphs`: `8678428ef9ea78cc046fe33a353098e90fdbd7349030c1836559ebcfd5a4bda5`

Fonti primarie:

- https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/
- https://github.com/schriftgestalt/GlyphsSDK
- https://github.com/kronenthaler/openstep-parser
