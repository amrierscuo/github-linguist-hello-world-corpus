# 0529 — Pascal: `.dpr`

Ruolo: Programma Delphi console con direttiva APPTYPE; mantiene entry point program.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Genuine Free Pascal compiler — 3.2.2. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
dcc32 hello.dpr; hello.exe (oppure FPC in modalità Delphi nel work locale)
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.dpr`: `f6580480e5910b62273a311a3f47fb5b897bf7ecb02c9d4e4ff326d7a7e2dba7`

Fonti primarie:

- https://docwiki.embarcadero.com/RADStudio/en/Programs_and_Units_(Delphi)
- https://www.freepascal.org/docs.html
