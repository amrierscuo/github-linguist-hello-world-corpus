# #005 ABAP CDS

`zi_hello_world.ddls.asddls` defines the view entity `ZI_Hello_World`: for each
customer present in the table SAP `T000` exposes `Client` and the constant value
`Hello, World!` in `Greeting` column. It is a data definition, not a
program that prints on console. The expected reading does not change `T000`.

## Toolchain and commands

Local Parsing: **Node.js 22** and **abaplint 2.120.70**. From the example folder:

```powershell
npm install --prefix .tools --ignore-scripts --no-audit --no-fund @abaplint/cli@2.120.70
node .tools/node_modules/@abaplint/cli/abaplint abaplint.json -f json
```

The `cds_parser_error` rule controls DDL grammar; expected result:
0 code and `[]`. The `v758` profile is normalized by this abaplint to `v793`
(on-premise 758 ), visible in the log.

Full check provided: **SAP ABAP Platform con supporto alle view entity**,
table `T000` accessible and **ABAP Development Tools (ADT)**. Create a Date
Definition `ZI_HELLO_WORLD`, insert the source and use `Activate` (Ctrl+F3).
Open `Data Preview` (F8) of the activated entity.
`Greeting = Hello, World!`. A separate compilation from activation is not required.

The ADT object must have the same name as the statement: `ZI_HELLO_WORLD`.
`T000` is an addiction to the classic system; the example does not assume that it is
a API released for ABAP Cloud.

## Status and limitations

syntax **verificata dal parser CDS di abaplint**; behavior **not yet
verified **. `verification/abaplint.json` includes a negative source
malformed, really rejected. Configuration does not solve the dictionary
for SAP and does not activate the object in the database. The required SAP/ADT system is unavailable
to complete the verification.

## Primary sources

- [SAP, CDS view entity e loro impiego](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/abencds_v2_views.htm).
- [SAP, regole DDL e stringhe tra apici singoli](https://help.sap.com/docs/ABAP_PLATFORM/f2e545608079437ab165c105649b89db/4ed24bd56e391014adc9fffe4e204223.html?version=1709.008).
- [abaplint, regole `cds_parser_error` e `cds_check_syntax`](https://rules.abaplint.org/).

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.asddls` | [zi_hello_world.ddls.asddls](zi_hello_world.ddls.asddls) syntax verified |
