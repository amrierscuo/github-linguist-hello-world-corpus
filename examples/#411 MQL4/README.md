# #411 MQL4

## Verified on November 22, 2026

The official MetaEditor compiled the original hello.mq4 into an EX4 file. The official MetaTrader 4 terminal ran the hello script from its startup configuration and recorded the exact `Hello, World!` greeting in the script log. It ran inside an isolated Xvfb display without network access and closed with exit code 0.

Run `metaeditor.exe /portable /compile:<absolute Windows path to hello.mq4> /log; terminal.exe /portable <absolute Windows path to terminal-start.ini>; request window close via Wine taskkill.exe /IM terminal.exe after observing the greeting`.

[Commands, toolchain, output and SHA-256](verification/native_20261122_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

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

</details>
