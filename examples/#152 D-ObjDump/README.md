# #152 D-ObjDump

The canonical entry and order come from the corpus's `reference/languages.yml`. Sources and fixtures are original; any dumps or bundles come from the stated tools.

## Goal

Produce an authentic disassembly of an original D object associated with a Hello, World! program.

hello.d-objdump è output testuale originale del vero objdump, non assembly scritto a mano. hello.d è la fixture da cui nasce l’oggetto. Il log conserva SHA-256 dell’oggetto e dei sorgenti, output del tool e esecuzione del programma. La semantica verificata è provenienza e associazione al programma; il dump non si esegue direttamente.

## Toolchain and reproduction

LDC 1.43.0 BetterC; GNU objdump/Binutils 2.42; Linux ELF x86_64

Commands in the example folder with the toolchain available in PATH. Use a temporary copy: databases, objects, audio and other test outputs do not belong to the corpus.

```text
ldc2 -betterC -c hello.d -of=hello.o
objdump -d -r -s hello.o > hello.d-objdump
```

```text
ldc2 -betterC hello.d -of=hello
./hello
Confrontare il dump rigenerato con hello.d-objdump.
```

## Expected result and status

Item ELF x86_64 real, sections and symbol greeting D present, literal Hello, World! in data; associated program issues greeting.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records versions and provenance, SHA-256 of the source, actual commands, exit, stdout and stderr normalized.

## Primary sources

- https://sourceware.org/binutils/docs/binutils/objdump.html
- https://dlang.org/spec/betterc.html
- https://github.com/ldc-developers/ldc/releases/tag/v1.43.0

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.d-objdump` | [hello.d-objdump](hello.d-objdump) verified |
