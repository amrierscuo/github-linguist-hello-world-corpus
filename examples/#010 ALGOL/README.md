# #010 ALGOL

## Verified on November 18, 2026

JFF compiled the unchanged ALGOL 60 program from its own native toolchain and the executable printed the greeting. The raw output retains the trailing NUL emitted by this runtime.

Run `jff-algol hello.alg; ./hello`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

[Earlier evidence](verification.log).

<details>
<summary>Earlier instructions and evidence</summary>

`hello.alg` is a ALGOL 60 program for the dialect and environment of I/O
**jff-algol**, which uses `outstring` and `newline` on the 1. channel
expected is a `Hello, World!` line. The canonical entry uses `source.algol60`;
for this the example adopts ALGOL 60 and explicitly declares the environment of I/O.

## Toolchain and commands

They serve jff-algol by Jan van Katwijk, his prelude and runtime, and a compiler
C in its Linux or Cygwin environment. From the example folder:

```sh
jff-algol hello.alg
./hello
```

The driver translates `hello.alg` into C, compiles and connects the `hello` executable.
To perform only front-end translation: `jff-algol -o hello.alg`.
Follow the manual to configure jff-algol and runtime paths.

## Status

created; syntax and behavior **non verificate**. There are no jff-algol or
its toolchain C/Cygwin in the PATH of the environment.
the syntax and the procedures documented by the author; this review of the sources
do not replace compilation. See `verification.log`.

## Primary source

- [Manuale dell'autore di jff-algol, conservato nell'archivio ALGOL](https://gtoal.com/languages/algol60/jff-algol-60-compiler/doc/jff-manual.pdf)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.alg` | [hello.alg](hello.alg) Syntax and behavior verified |

</details>
