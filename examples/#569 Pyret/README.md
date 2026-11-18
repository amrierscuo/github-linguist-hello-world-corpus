# #569 Pyret

## Verified on November 18, 2026

The official Pyret compiler translated the exact source. Running its generated program emitted the original greeting.

Run `pyret --port <private-socket> hello.arr --outfile greeting.jarr; node greeting.jarr with the pinned npm dependency directory`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Evaluate the original Pyret program.

## Toolchain

Pyret compiler/runtime

## Procedure

Open hello.arr in code.pyret.org and press Run; or use official CLI of the registered version.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- Compiler/runtime Pyret non predisposto; valutazione pending.

## Primary sources

- [https://pyret.org/docs/latest/](https://pyret.org/docs/latest/)
- [https://code.pyret.org/](https://code.pyret.org/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.arr` | [hello.arr](hello.arr) Syntax and behavior verified |

</details>
