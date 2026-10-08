# 0333 — Java: `.jsh`

Ruolo: Script JShell con istruzione top-level, distinto da classe Java compilabile.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: OpenJDK 21.0.12. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
jshell hello.jsh
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.jsh`: `40c7451ecae69a32ad31a09b931c43d2ee15570efac83d6d59f9ed5f8771f238`

Fonti primarie:

- https://docs.oracle.com/en/java/javase/21/jshell/introduction-jshell.html
- https://docs.oracle.com/javase/tutorial/getStarted/cupojava/win32.html
