# #669 Smali

Assemble Smali in DEX with a main method that prints greeting.

Canonical type `programming`, language_id `351`.

Suggested toolchain: Google smali assembler and Android ART/Dalvik for execution.

From the example directory:

```sh
smali assemble Hello.smali -o build/hello.dex
```

Expected result: DEX valid; main Hello, World! print on the Android runtime.

Assembling the DEX does not prove the ART execution; this remains distinct.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [Smali](https://github.com/google/smali)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.smali` | [Hello.smali](Hello.smali) created; verification pending |
