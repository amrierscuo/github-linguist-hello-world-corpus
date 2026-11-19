# #385 Limbo

## Verified on November 19, 2026

The compatible native Limbo compiler compiled the original module and the real Dis emulator invoked its init function, emitting the exact greeting.

Run `limbo -I <inferno module dir> -o hello.dis hello.b && emu -r <tree> -c1 /dis/hello-corpus.dis`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Fill out a Limbo module for Inferno that uses Sys->print.

## Toolchain

Inferno/Limbo; versione da registrare

## Commands and procedure

In the runtime Inferno: limbo -o hello.dis hello.b;./ hello.dis

## Expected result

Sys charging module and writes Hello, World! more newline.

## Status

Syntax and behavioral verification pending.

init exposes the Inferno shell interface and loads the authentic Sys module. Sys/Draw interfaces come from the runtime; they are not stub included in the corpus.

Remaining requirements:
- Filler Limbo and VM Dis Inferno not available; import Sys/Draw and runtime pending.

## Primary sources

- [https://www.vitanuova.com/inferno/limbo.html](https://www.vitanuova.com/inferno/limbo.html)
- [https://www.vitanuova.com/inferno/papers/limbo.html](https://www.vitanuova.com/inferno/papers/limbo.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.b` | [hello.b](hello.b), [hello.b](variants/m-f7140aa0/hello.b) created; verification pending |
| `.m` | [hello.m](variants/m-f7140aa0/hello.m) created; verification pending |

</details>
