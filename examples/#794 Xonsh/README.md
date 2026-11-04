# #794 Xonsh

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Eseguire Xonsh e stampare Hello, World!.

The authentic parser/runtime Xonsh scripts. The log also keeps the notice of the absence of readline for interactive use; the greeting is the final line and the test does not use an interactive shell.

## Toolchain and reproduction

Xonsh0.24.2 originale, Python3.13

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
python -m xonsh --no-rc --shell-type dumb hello.xsh
```

## Expected result and status

Exit0 e riga finale Hello, World! su stdout.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://xon.sh/tutorial.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.xsh` | [hello.xsh](hello.xsh) verified |
