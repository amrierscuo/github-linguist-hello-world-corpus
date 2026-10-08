# 0593 — RPGLE — `.sqlrpgle`

RPG free form con embedded SQL; necessita SQL precompiler IBM i.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.sqlrpgle`.

Controllo previsto, dalla cartella della variante:

```text
IBM i CRTSQLRPGI OBJ(TESTLIB/HELLO) SRCSTMF(hello.sqlrpgle); CALL TESTLIB/HELLO
```

Risultato atteso: display Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://www.ibm.com/docs/en/i/7.5.0?topic=applications-coding-sql-statements-in-ile-rpg](https://www.ibm.com/docs/en/i/7.5.0?topic=applications-coding-sql-statements-in-ile-rpg)
