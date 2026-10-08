# 0503 — OpenEdge ABL: `.cls`

Ruolo: Classe ABL con metodo statico Greeting, distinto dalla procedura .p.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Progress OpenEdge ABL. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
OpenEdge: compilare CorpusGreeting.cls e driver.p; eseguire driver in sessione di test
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `CorpusGreeting.cls`: `3aef1f12e6194253b8816630a77925b91adb49c0dd217b549995866241085261`
- `driver.p`: `50db11866901900381077e0c98deb980df85de30cfdc2f8c0e9be7b9db3ec34c`

Fonti primarie:

- https://docs.progress.com/bundle/abl-reference/page/CLASS-statement.html
- https://docs.progress.com/bundle/abl-reference/page/MESSAGE-statement.html
