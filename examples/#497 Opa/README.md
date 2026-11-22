# #497 Opa

## Verified on November 22, 2026

The native Opa compiler accepted the original hello.opa. The generated JavaScript ran with the Opa runtime in a private network namespace. A loopback HTTP request returned status 200 and the page contained an h1 element whose exact text was Hello, World!

Run `opa -o corpus-greeting.js hello.opa; node corpus-greeting.js --port 8080; GET http://127.0.0.1:8080/`.

[Commands, toolchain, output and SHA-256](verification/native_20261122_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Serve an Opa page containing greeting.

## Toolchain

Opa web compiler, syntax JS -like

## Procedure

opa --parser js-like hello.opa --; read the local HTTP page of the actual port

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

Server.start and syntax page:function are conform to the canonical sample; check the option of the compiler chosen before the test.

Remaining requirements:
- Filler Opa web historical and runtime Node required not predisposed.

## Primary sources

- [https://github.com/MLstate/opalang](https://github.com/MLstate/opalang)
- [https://github.com/github-linguist/linguist/blob/main/samples/Opa/hello_syntax2.opa](https://github.com/github-linguist/linguist/blob/main/samples/Opa/hello_syntax2.opa)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.opa` | [hello.opa](hello.opa) Syntax and behavior verified |

</details>
