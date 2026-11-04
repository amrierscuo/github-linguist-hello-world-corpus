# #491 ObjectScript

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
| `.cls` | [Hello.cls](Hello.cls) created; verification pending |
