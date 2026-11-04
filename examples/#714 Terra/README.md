# #714 Terra

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Fill out JIT a Terra function and print Hello, World!.

The host Lua program declares a ground function, imports stunt and invokes it; Lua without Earth does not perform this language.

## Toolchain and reproduction

Terra con LLVM/Clang, versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
terra hello.t
```

## Expected result and status

Hello, World! su stdout.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Impedimenti: Terra runtime non predisposto; verifica JIT e chiamata C pendenti.

## Primary sources

- https://terralang.org/getting-started.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.t` | [hello.t](hello.t) created; verification pending |
