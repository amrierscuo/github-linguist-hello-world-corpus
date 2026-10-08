# 0397 — Logos: `.x`

Ruolo: Logos senza preprocessing C automatico: %ctor Objective-C di saluto.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Theos Logos master snapshot; This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Theos Logos: logos.pl hello.x > generated.m; compilare ObjC con import Foundation nel progetto iOS di test
```

Risultato atteso: Log iOS con Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.x`: `3dcc29dcd2e4cb81135612064a23ea5a8d7fa50e774cf8b4daae8b3f2c43ff09`

Fonti primarie:

- https://theos.dev/docs/logos
- https://theos.dev/docs/logos-syntax
- https://github.com/theos/logos
