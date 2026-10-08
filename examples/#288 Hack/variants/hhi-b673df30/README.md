# 0288 — Hack: `.hhi`

Ruolo: Interfaccia Hack HHI con sola dichiarazione; l’implementazione è nel fixture .hack.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: HHVM/Hack e typechecker hh_client; versioni effettive da registrare. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
hh_client in progetto che espone hello.hhi e la relativa implementazione; hhvm driver.hack
```

Risultato atteso: Dichiarazione di greeting(): string; driver stampa Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.
- HHI e implementazione devono essere configurati come interfaccia di libreria esterna, evitando dichiarazioni duplicate nello stesso progetto.

SHA-256 dei file della variante:

- `driver.hack`: `f0d3a9127b2b5314d4505c825137f6aa22e3e95e47aa32098a8d2af349498045`
- `hello.hhi`: `3bfa59fd2f621765b13cc70311275bf02f3dbdb63efb3fd22fb3f7309b195ce9`

Fonti primarie:

- https://docs.hhvm.com/hack/getting-started/getting-started
- https://docs.hhvm.com/hack/source-code-fundamentals/program-structure/
- https://hacklang.org/
