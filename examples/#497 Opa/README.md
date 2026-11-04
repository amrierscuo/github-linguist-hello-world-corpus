# #497 Opa

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
| `.opa` | [hello.opa](hello.opa) created; verification pending |
