# #173 E

## Verified on November 18, 2026

The archived E-on-Java interpreter evaluated the original console sample and emitted the exact greeting.

Run `java -cp <E runtime and dependencies> org.erights.e.elang.interp.Rune hello.e`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Eseguire println in E e stampare Hello, World!.

## Toolchain

E-on-Java ERights, launcher rune e JVM compatibile; versioni da registrare

## Commands and procedure

rune hello.e

## Expected result

Interpreter E exit 0, stdout Hello, World! plus newline.

## Status

Syntax and behavioral verification pending.

The voice is the E language of ERights. println is a function of its standard environment; it is not assumed that a .e compiler of other language is compatible.

Remaining requirements:
- Runtime E-on-Java/rune compatible not predisposed; interpreter E not executed.

## Primary sources and format reference

- [https://www.erights.org/](https://www.erights.org/)
- [https://erights.org/elang/kernel/auditors/index.html](https://erights.org/elang/kernel/auditors/index.html)
- [https://erights.org/download/0-8-14/index.html](https://erights.org/download/0-8-14/index.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.e` | [hello.e](hello.e) Syntax and behavior verified |

</details>
