# #412 MQL5

## Verified on November 22, 2026

MetaEditor compiled the original hello.mq5 into an EX5 file. The official MetaTrader 5 terminal ran the compiled script from its startup configuration and recorded `Hello, World!` in the script log. Compilation and execution used a private virtual display and a network-isolated Wine prefix with Wine Mono disabled.

Run `metaeditor64.exe /portable /compile:<hello.mq5> /log:<compile.log> followed by terminal64.exe /portable /config:<terminal-start.ini>`.

[Commands, toolchain, output and SHA-256](verification/native_20261122_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

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

</details>
