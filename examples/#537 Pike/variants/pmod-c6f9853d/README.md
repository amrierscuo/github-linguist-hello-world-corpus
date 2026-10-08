# 0537 — Pike: `.pmod`

Ruolo: Modulo Pike con funzione greeting; driver usa compile_file.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Genuine Pike language interpreter — Pike v8.0 release 1738 Copyright © 1994-2022 Linköping University; Pike comes with ABSOLUTELY NO WARRANTY; This is free software and you are; welcome to redistribute it under certain conditions; read the files; COPYING and COPYRIGHT in the Pike distribution for more details.. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
pike driver.pike
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `driver.pike`: `36e426eddaf91634160a0161c42786112ad3fc9fe3a27e9a52e7136160d5558b`
- `hello.pmod`: `eed01d39064c3a993ca9964cd24697fea5decd5fff30016bf8e902f910dd28b8`

Fonti primarie:

- https://pike.lysator.liu.se/docs/tutorial/
- https://pike.lysator.liu.se/docs/man/
