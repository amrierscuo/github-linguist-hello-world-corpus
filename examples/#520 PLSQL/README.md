# #520 PLSQL

Eseguire un blocco Oracle PL/SQL e leggere il buffer DBMS_OUTPUT.

Tipo canonico `programming`, language_id `273`.

Toolchain prevista: Oracle Database e SQL*Plus.

Dalla cartella dell’esempio:

```sh
sqlplus <connessione-di-prova> @hello.sql
```

Risultato atteso: DBMS_OUTPUT contiene Hello, World!.

SET SERVEROUTPUT è una direttiva SQL*Plus; non sono necessarie tabelle o mutazioni di dati.

Stato iniziale: creato; sintassi e semantica in attesa. Oracle Database di prova e client SQL*Plus non disponibili.

Fonti:

- [Oracle DBMS_OUTPUT](https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pls` | [hello.pls](variants/pls-3dffc841/hello.pls) creato, verifiche pendenti |
| `.bdy` | [hello.bdy](variants/bdy-4c34a409/hello.bdy) creato, verifiche pendenti |
| `.ddl` | [hello.ddl](variants/ddl-8bc7bf69/hello.ddl) creato, verifiche pendenti |
| `.fnc` | [hello.fnc](variants/fnc-45334aa2/hello.fnc) creato, verifiche pendenti |
| `.pck` | [hello.pck](variants/pck-1454aec3/hello.pck) creato, verifiche pendenti |
| `.pkb` | [hello.pkb](variants/pkb-3cd1ab70/hello.pkb) creato, verifiche pendenti |
| `.pks` | [hello.pks](variants/pks-3b8251b6/hello.pks) creato, verifiche pendenti |
| `.plb` | artefatto da generare Output del PL/SQL wrap utility, non sorgente testuale ordinario. Il wrapper Oracle originale non è disponibile: non si fabbrica una sequenza wrapped. |
| `.plsql` | [hello.plsql](variants/plsql-b119d779/hello.plsql) creato, verifiche pendenti |
| `.prc` | [hello.prc](variants/prc-8feafefc/hello.prc) creato, verifiche pendenti |
| `.spc` | [hello.spc](variants/spc-3e58c266/hello.spc) creato, verifiche pendenti |
| `.sql` | [hello.sql](hello.sql), [spec.sql](variants/bdy-4c34a409/spec.sql), [spec.sql](variants/pkb-3cd1ab70/spec.sql), [body.sql](variants/pks-3b8251b6/body.sql), [body.sql](variants/spc-3e58c266/body.sql), [spec.sql](variants/tpb-372a8945/spec.sql), [body.sql](variants/tps-599a8ac3/body.sql) creato, verifiche pendenti |
| `.tpb` | [hello.tpb](variants/tpb-372a8945/hello.tpb) creato, verifiche pendenti |
| `.tps` | [hello.tps](variants/tps-599a8ac3/hello.tps) creato, verifiche pendenti |
| `.trg` | [hello.trg](variants/trg-cb798897/hello.trg) creato, verifiche pendenti |
| `.vw` | [hello.vw](variants/vw-2cbbc276/hello.vw) creato, verifiche pendenti |
