# 0397 — Logos: `.xi`

Ruolo: Include Logos non-preprocessato: definizione funzione, non %ctor duplicato.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Theos Logos master snapshot; This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Theos: includere hello.xi nel sorgente .x; invocare corpusGreeting da %ctor
```

Risultato atteso: Hello, World! nel log

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.xi`: `38f12e3822ce5b4af1b6e32307ffe2ef98950bcea03d07fdf481bff911fdb37c`

Fonti primarie:

- https://theos.dev/docs/logos-file-extensions
- https://theos.dev/docs/logos
- https://theos.dev/docs/logos-syntax
- https://github.com/theos/logos
