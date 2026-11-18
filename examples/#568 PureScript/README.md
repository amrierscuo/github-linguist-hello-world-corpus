# #568 PureScript

## Verified on November 18, 2026

The native PureScript compiler compiled the original main. Node executed the compiler-generated JavaScript and printed the exact greeting.

Run `purs compile Main.purs <prelude, effect and console library sources>; import output/Main/index.js and invoke main() with Node`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Fill PureScript and run main.

## Toolchain

PureScript purs; effect/console/Prelude; Node.js

## Procedure

In the compatible Spago project copy Main.purs in src; spago build; spago run

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- Compilatore purs e librerie Spago compatibili non predisposti.

## Primary sources

- [https://www.purescript.org/](https://www.purescript.org/)
- [https://github.com/purescript/purescript-console](https://github.com/purescript/purescript-console)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.purs` | [Main.purs](Main.purs) Syntax and behavior verified |

</details>
