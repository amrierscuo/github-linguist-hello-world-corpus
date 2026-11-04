# #408 MAXScript

Write greetings in the MAXScript Listener.

Canonical type `programming`, language_id `217`.

Suggested toolchain: Autodesk 3ds Max MAXScript runtime.

From the example directory:

```sh
Eseguire fileIn "hello.ms" nel MAXScript Listener di una scena di prova.
```

Expected result: Listener shows Hello, World! and newline.

No operation on the scene; verification requires the MAXScript owner runtime.

Initial state: created; syntax and behavioral verification pending. Runtime Autodesk 3ds Max unavailable.

Sources:

- [Autodesk — MAXScript format](https://help.autodesk.com/view/MAXDEV/2026/ENU/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ms` | [hello.ms](hello.ms) created; verification pending |
| `.mcr` | [hello.mcr](variants/mcr-27698a41/hello.mcr) created; verification pending |
