# #035 Apollo Guidance Computer

Represent Hello, World! with 13 words AGC containing ASCII numerical codes; the Block II program loads the first code (H, 00110 octal) in the A register and remains in the HOLD cycle.

## File

- `hello.agc`

## Toolchain and verification

Virtual AGC yaYUL revision 2017-06-19, Windows 2017-08-31 distribution; yaAGC emulator for residual CPU verification.

`OCT` inserts 15 bit optic constants in the assembled memory.
character of greeting occupies a word: it is not a code used historically
by DSKY, but an explicit convention of the sample. `CA GREET` charge H in the
A register; `TC HOLD` maintains control in a cycle.

```text
yaYUL hello.agc
```

The command produces `hello.agc.bin` and `hello.agc.symtab` in the workbook;
use a temporary copy of the source to keep these derivatives separate.
The test assembler declares the 2017-06-19 revision in its header.

Test CPU yet required: load the core-rope in a yaAGC block II instance,
use the debugger to set the program counter Z to 04000, run `CA`,
observe A= 00110 and the cycle on the next `HOLD`; read the thirteen words
by `GREET` as numerical ASCII values to rebuild Hello, World!.
This protocol has not been executed and there is no proof of print.

## Expected result

Assembly exit 0, zero errori fatali e warning. Obiettivo CPU: A=00110 e HOLD ripetuto; codici dati 00110 00145 00154 00154 00157 00054 00040 00127 00157 00162 00154 00144 00041.

## State of the test

syntax verified. behavioral verification pending.

The greeting uses an explicit ASCII convention in this sample. The complete assembly step ran; CPU semantics were not verified.

Actual Windows x64 test of 2026-10-08T11:01:56.068379+00:00: [log](verification/result.json).
The log includes hash SHA-256 of the source, observed versions, commands, exit codes, stdout and stderr.

Remaining requirements:
- There is no CPU test in yaAGC: A register and HOLD cycle not observed. AGC does not have a text console; no print is declared.

## Primary sources

- [https://www.ibiblio.org/apollo/assembly_language_manual.html](https://www.ibiblio.org/apollo/assembly_language_manual.html)
- [https://www.ibiblio.org/apollo/yaYUL.html](https://www.ibiblio.org/apollo/yaYUL.html)
- [https://github.com/virtualagc/virtualagc](https://github.com/virtualagc/virtualagc)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.agc` | [hello.agc](hello.agc) syntax verified |
