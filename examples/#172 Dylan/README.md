# #172 Dylan

Fill out an executable Dylan library and write Hello, World! with format-out.

## Toolchain

Open Dylan con librerie common-dylan/io; versione concreta da registrare

## Commands and procedure

dylan-compiler -build hello.lid; _build/bin/hello

## Expected result

Filling and linking exit 0; executable print the greeting more newline.

## Status

Syntax and behavioral verification pending.

library.dylan declares library and module, hello.lid first lists the statement and then the program. The program uses the format-out module console format. Dylan toolchain has not been replaced with a generic parser.

Remaining requirements:
- Toolchain Open Dylan e librerie non predisposte; compilazione/linking/esecuzione pending.

## Primary sources and format reference

- [https://opendylan.org/getting-started-cli/hello-world.html](https://opendylan.org/getting-started-cli/hello-world.html)
- [https://opendylan.org/library-reference/io/format-out.html](https://opendylan.org/library-reference/io/format-out.html)
- [https://opendylan.org/download/index.html](https://opendylan.org/download/index.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.dylan` | [hello.dylan](hello.dylan), [library.dylan](library.dylan) created; verification pending |
| `.dyl` | [hello.dyl](variants/ext-dyl-2e64796c/hello.dyl) created; verification pending |
| `.intr` | [hello.intr](variants/ext-intr-2e696e7472/hello.intr) created; verification pending |
| `.lid` | [hello.lid](hello.lid) created; verification pending |
