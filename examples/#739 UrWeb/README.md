# #739 UrWeb

Fill out a UrWeb page and read it via local HTTP.

## Toolchain

UrWeb compiler/runtime

## Procedure

urweb hello;./ hello.exe; read the main page from the local port indicated.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- UrWeb compiler/runtime e dipendenze native non predisposti.

## Primary sources

- [https://www.impredicative.com/ur/tutorial/](https://www.impredicative.com/ur/tutorial/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ur` | [hello.ur](hello.ur), [hello.ur](variants/urs-27e086e7/hello.ur) created; verification pending |
| `.urs` | [hello.urs](variants/urs-27e086e7/hello.urs) created; verification pending |
