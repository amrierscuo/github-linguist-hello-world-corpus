# #491 ObjectScript

## Verified on November 19, 2026

The genuine IRIS compiler loaded the original class. A USER terminal session invoked Corpus.Hello.Greet and returned the exact greeting.

Run `sh iris-local.sh inside the digest-verified IRIS Community image`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Fill in an InterSystems class and invoke Greet.

## Toolchain

InterSystems IRIS ObjectScript

## Procedure

In the test namespace: do $ SYSTEM.OBJ.Load ( "Hello.cls", "ck" ) then do ##class( Corpus.Hello ) .Greet ()

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- InterSystems IRIS compiler/namespace unavailable.

## Primary sources

- [https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=GCOS](https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=GCOS)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cls` | [Hello.cls](Hello.cls) Syntax and behavior verified |

</details>
