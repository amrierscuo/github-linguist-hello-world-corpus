# 0344 — Jolie: `.iol`

Ruolo: Interfaccia Jolie include: dichiarazione di tipo e one-way GreetingPort; implementazione nel fixture.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Required genuine toolchain not available/configured — non disponibile / non verificata. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Jolie: include hello.iol in progetto di test e compilare l’interfaccia; inviare greet con Hello, World! solo se host disponibile
```

Risultato atteso: Interfaccia accettata e dato Greeting stringa

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.iol`: `1ed4d8c1416ca7dc3ee7d5f6768f912bfa55331199ff1973a4e74f6ac46f9816`

Fonti primarie:

- https://docs.jolie-lang.org/v1.13.x/language-tools-and-standard-library/basics/interfaces.html
- https://www.jolie-lang.org/
- https://docs.jolie-lang.org/v1.12.x/language-tools-and-standard-library/basics/fault-handling/scopes-and-faults/README.html
- https://github.com/jolie/jolie
