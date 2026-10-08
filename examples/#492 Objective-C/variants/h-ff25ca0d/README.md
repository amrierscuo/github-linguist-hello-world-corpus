# 0492 — Objective-C: `.h`

Ruolo: Header Objective-C con dichiarazione della funzione del saluto; implementazione e driver a parte.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0; GNU libobjc4 14.2.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
clang/GNUstep o Xcode: compilare greeting.m che importa hello.h; link Foundation e avviare
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `greeting.m`: `db0f805d693d166be828dc4d5f3a54b6a4e51454cb8c65e3f1c1958339cdbdac`
- `hello.h`: `6691c033ea05a9027640445c1ea37b8440b50c75b640db4fa99aff4b9ea76e13`

Fonti primarie:

- https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/
- https://gcc.gnu.org/onlinedocs/gcc/Objective-C.html
