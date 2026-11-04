# #472 Nim

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Fill in Nim and print Hello, World!.

let lega una stringa, & concatena e echo effettua l’IO. Il compiler originale esegue parsing/typecheck e produce il programma C compilato da GCC; binario e cache restano in work.

## Toolchain and reproduction

Nim1.6.14 Ubuntu, backend C/GCC

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
nim c --out:hello hello.nim
```

```text
./hello
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://nim-lang.org/docs/tut1.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.nim` | [hello.nim](hello.nim), [hello.nim](variants/nim-cfg-a023dc1f/hello.nim) created; verification pending |
| `.nim.cfg` | [hello.nim.cfg](variants/nim-cfg-a023dc1f/hello.nim.cfg) created; verification pending |
| `.nimble` | [hello.nimble](variants/nimble-ba115bce/hello.nimble) created; verification pending |
| `.nimrod` | [hello.nimrod](variants/nimrod-b772c342/hello.nimrod) created; verification pending |
| `.nims` | [hello.nims](variants/nims-27124d6b/hello.nims) created; verification pending |
