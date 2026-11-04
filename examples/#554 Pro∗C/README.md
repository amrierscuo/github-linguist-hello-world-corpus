# #554 Pro*C

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Precompilare Pro*C e stampare la variabile host greeting=Hello, World!.

EXEC SQL BEGIN/END DECLARE SECTION gives greeting to a Pro*C host variable. The program does not require a query or an Oracle connection for greeting; the precompiler remains necessary to control the directives.

## Toolchain and reproduction

Oracle Pro*C/C++ precompiler e compiler C; versioni da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
proc iname=hello.pc; cc hello.c -o hello
```

```text
./hello
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: Precompiler Oracle Pro*C unavailable; GCC on the C alone does not verify the EXEC SQL directives.

## Primary sources

- https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpcc/c-c-programmers-guide.pdf

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pc` | [hello.pc](hello.pc) created; verification pending |
