# #520 PLSQL

Perform an Oracle PL/SQL block and read the DBMS_OUTPUT buffer.

Canonical type `programming`, language_id `273`.

Suggested toolchain: Oracle Database and SQL *Plus.

From the example directory:

```sh
sqlplus <connessione-di-prova> @hello.sql
```

Expected result: DBMS_OUTPUT contains Hello, World!.

SET SERVEROUTPUT is a SQL *Plus directive; no tables or data mutations are required.

Initial state: created; syntax and behavioral verification pending. Oracle Test database and SQL*Plus clients not available.

Sources:

- [Oracle DBMS_OUTPUT](https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pls` | [hello.pls](variants/pls-3dffc841/hello.pls) created; verification pending |
| `.bdy` | [hello.bdy](variants/bdy-4c34a409/hello.bdy) created; verification pending |
| `.ddl` | [hello.ddl](variants/ddl-8bc7bf69/hello.ddl) created; verification pending |
| `.fnc` | [hello.fnc](variants/fnc-45334aa2/hello.fnc) created; verification pending |
| `.pck` | [hello.pck](variants/pck-1454aec3/hello.pck) created; verification pending |
| `.pkb` | [hello.pkb](variants/pkb-3cd1ab70/hello.pkb) created; verification pending |
| `.pks` | [hello.pks](variants/pks-3b8251b6/hello.pks) created; verification pending |
| `.plb` | artifact to generate PL/SQL wrap utility output, not ordinary text source. The original Oracle wrapper is not available: no wrapped sequence is manufactured. |
| `.plsql` | [hello.plsql](variants/plsql-b119d779/hello.plsql) created; verification pending |
| `.prc` | [hello.prc](variants/prc-8feafefc/hello.prc) created; verification pending |
| `.spc` | [hello.spc](variants/spc-3e58c266/hello.spc) created; verification pending |
| `.sql` | [hello.sql](hello.sql), [spec.sql](variants/bdy-4c34a409/spec.sql), [spec.sql](variants/pkb-3cd1ab70/spec.sql), [body.sql](variants/pks-3b8251b6/body.sql), [body.sql](variants/spc-3e58c266/body.sql), [spec.sql](variants/tpb-372a8945/spec.sql), [body.sql](variants/tps-599a8ac3/body.sql) created; verification pending |
| `.tpb` | [hello.tpb](variants/tpb-372a8945/hello.tpb) created; verification pending |
| `.tps` | [hello.tps](variants/tps-599a8ac3/hello.tps) created; verification pending |
| `.trg` | [hello.trg](variants/trg-cb798897/hello.trg) created; verification pending |
| `.vw` | [hello.vw](variants/vw-2cbbc276/hello.vw) created; verification pending |
