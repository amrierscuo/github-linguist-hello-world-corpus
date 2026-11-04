# #411 MQL4

Run a MQL4 script that writes greeting in the local registry.

Canonical type `programming`, language_id `426`.

Suggested toolchain: MetaTrader 4 MetaEditor/compiler.

From the example directory:

```sh
Compilare hello.mq4 in MetaEditor; eseguire lo script nel terminale di prova.
```

Expected result: compilation without errors; Experts register contains Hello, World!.

It does not open orders, does not read accounts and does not use network. It is a local script, not an expert advisor operating.

Initial state: created; syntax and behavioral verification pending. Toolchain MetaTrader 4 unavailable.

Sources:

- [MetaQuotes — MQL4 OnStart](https://docs.mql4.com/basis/function/events#onstart)
- [MetaQuotes — Print](https://docs.mql4.com/common/print)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mq4` | [hello.mq4](hello.mq4), [driver.mq4](variants/mqh-c969556a/driver.mq4) created; verification pending |
| `.mqh` | [hello.mqh](variants/mqh-c969556a/hello.mqh) created; verification pending |
