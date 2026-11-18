# #445 Moocode

## Verified on November 18, 2026

The native LambdaMOO evaluator executed the exact original statement in a fixture database. Its synthetic player tell verb received the greeting, which the engine recorded in its server log.

Run `moo -e Minimal.db test.db <commands.txt`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

[Earlier evidence](verification/native.json).

<details>
<summary>Earlier instructions and evidence</summary>

Voce canonica `Moocode`, tipo `programming`, language_id `237`.

Send greeting to the player through a Moocode verb body.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

It requires LambdaMOO servers and databases with player:tell, as well as an authorized test player.

Comando/procedura from the directory of the example, unless explicit indications:

```text
In un server LambdaMOO locale con database LambdaCore: creare un verb greeting sul player, caricare hello.moo con @program, quindi invocare player:greeting().
```

Expected result: Hello, World!

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Corpo di verb originale; server/database mancanti, compilazione ed esecuzione pending.

Remaining requirements:

- LambdaMOO-compatible server/database with a test verb and player is not available.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.moo.mud.org/](https://www.moo.mud.org/)
- [https://github.com/wrog/lambdamoo](https://github.com/wrog/lambdamoo)
- [https://www.wrog.net/moo/pm1.8.1/ProgrammersManual.pdf](https://www.wrog.net/moo/pm1.8.1/ProgrammersManual.pdf)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.moo` | [hello.moo](hello.moo) Syntax and behavior verified |

</details>
