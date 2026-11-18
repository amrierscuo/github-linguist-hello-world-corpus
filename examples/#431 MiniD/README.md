# #431 MiniD

## Verified on November 18, 2026

The published MiniD successor loaded the unchanged original source and its console runtime printed the exact expected greeting.

In a scratch copy, run `cp test.minid test.croc; croc test.croc`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

The textbook requested by the user, saved in `test.minid`. The file begins with `module test` and contains the call `writeln` proposed in the chat. The required result is `Hello, world!`.

## Status and reproduction

Artefact created as **bozza fornita dall'utente**. syntax and behavior not verified: the historical MiniD runtime and its grammar have not been controlled. Croc is not used as a substitute for MiniD.

Procedure: with the appropriate MiniD 2 runtime, caricare/eseguire `test.minid` module and check the greeting. The exact command depends on the historical distribution and remains to be confirmed.

## Provenance

- Snippet provided by the user in this chat.
- Riferimento storico da recuperare: http://www.dsource.org/projects/minid/wiki/StdLib/BaseLib

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.minid` | [test.minid](test.minid) Syntax and behavior verified |

</details>
