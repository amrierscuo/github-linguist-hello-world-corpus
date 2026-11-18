# #739 UrWeb

## Verified on November 18, 2026

The native Ur/Web compiler built the original project. Its local executable handled an HTTP request and returned the exact greeting in the document body.

Run `urweb hello; ./hello.exe -a 127.0.0.1 -p <isolated port>; curl /Hello/main`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

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

</details>
