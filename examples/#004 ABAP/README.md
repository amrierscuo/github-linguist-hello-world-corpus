# #004 ABAP

`zhello_world.prog.abap` is a classic ABAP executable report. `WRITE` inserts
`Hello, World!` in the output list; `/` begins a new line.

## Toolchain and commands

Controllo statico: **Node.js 22** e **abaplint 2.120.70**. Installazione locale
isolated, from the example folder:

```powershell
npm install --prefix .tools --ignore-scripts --no-audit --no-fund @abaplint/cli@2.120.70
node .tools/node_modules/@abaplint/cli/abaplint abaplint.json -f json
```

The active configuration `parser_error` and `check_syntax`. The expected result is
0 output code and JSON blank `[]` list. The configured `v758` target is
normalized by this version of abaplint to its profile `v793` (on-premise 758 ),
as reported in the log.

Runtime verification: create `ZHELLO_WORLD` report in a system ** SAP AS ABAP
classic**, import the source, use sintassi/attivazione control and then
`Execute` (F8) in ABAP Editor. The list must contain `Hello, World!`.
There is no local executable to be compiled separately.

## Status and limitations

syntax **verificata staticamente** con abaplint; behavior di esecuzione
**non ancora verificata**. `verification/abaplint.json` also records a
negative control: a malformed string is rejected by the same analyzer.
There is no SAP system available. Static control does not constitute
a SAP activation or check the rendering of the list.

## Primary sources

- [SAP, istruzione `WRITE`](https://help.sap.com/docs/SAP_NETWEAVER_701/6da3d9466c4b1014a5a2e370bd8c5dc8/4a49ea1bea8b1c46e10000000a42189c.html).
- [SAP, programmi eseguibili e `REPORT`](https://help.sap.com/saphelp_scm700_ehp02/helpdata/en/fc/eb2d5a358411d1829f0000e829fbfe/content.htm?no_cache=true).
- [abaplint, progetto del verificatore](https://github.com/abaplint/abaplint).

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.abap` | [zhello_world.prog.abap](zhello_world.prog.abap) syntax verified |
