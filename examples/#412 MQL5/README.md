# #412 MQL5

Run a MQL5 script that writes greeting in the local registry.

Canonical type `programming`, language_id `427`.

Suggested toolchain: MetaTrader 5 MetaEditor/compiler.

From the example directory:

```sh
Compilare hello.mq5 in MetaEditor; eseguire lo script nel terminale di prova.
```

Expected result: compilation without errors; Experts register contains Hello, World!.

Example distinct from MQL4. No trading or communication functions.

Initial state: created; syntax and behavioral verification pending. Toolchain MetaTrader 5 unavailable.

Sources:

- [MetaQuotes — MQL5 OnStart](https://www.mql5.com/en/docs/event_handlers/onstart)
- [MetaQuotes — MQL5 Print](https://www.mql5.com/en/docs/common/print)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mq5` | [hello.mq5](hello.mq5), [driver.mq5](variants/mqh-c969556a/driver.mq5) created; verification pending |
| `.mqh` | [hello.mqh](variants/mqh-c969556a/hello.mqh) created; verification pending |
