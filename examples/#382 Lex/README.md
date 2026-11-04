# #382 Lex

Generate a Lex lexer that recognizes hello and Hello, World! print.

## Toolchain

flex 2.6.4; GCC 13.3.0

## Commands and procedure

flex -o build/hello.c hello.l; gcc build/hello.c -o build/hello; build/hello < input.txt

## Expected result

Scanner exit 0; a Hello, World! line.

## Status

syntax and behavior verified.

Regex and actions are interpreted by the original Flex, the generated C is compiled and executed. Spazi/newline are ignored; unexpected characters produce error. input.txt makes the scan reproducible.

Actual verification of 2026-10-08T12:48:20.760493+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://westes.github.io/flex/manual/](https://westes.github.io/flex/manual/)
- [https://westes.github.io/flex/manual/Simple-Examples.html](https://westes.github.io/flex/manual/Simple-Examples.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.l` | [hello.l](hello.l) verified |
| `.lex` | [hello.lex](variants/lex-9335749c/hello.lex) created; verification pending |
