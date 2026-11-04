# #800 Yacc

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Generate a Yacc parser and recognize the greeting of the fixture.

Bison genera il parser dalla grammatica .y; Flex genera il lexer originale complementare. Il parser compilato legge input.txt ed esegue l’azione solo dopo riconoscimento.

## Toolchain and reproduction

GNU Bison3.8.2 compatibile Yacc, Flex2.6.4, M4 e GCC originali

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
bison -d hello.y; flex lexer.l; gcc hello.tab.c lex.yy.c -o hello; ./hello < input.txt
```

## Expected result and status

Fixture riconosciuta, exit0 e Hello, World! su stdout.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.gnu.org/software/bison/manual/bison.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.y` | [hello.y](hello.y) verified |
| `.yacc` | [hello.yacc](variants/yacc-a86b8c02/hello.yacc) created; verification pending |
| `.yy` | [hello.yy](variants/yy-d3b03e84/hello.yy) created; verification pending |
