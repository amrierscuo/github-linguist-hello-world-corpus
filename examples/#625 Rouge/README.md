# #625 Rouge

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Eseguire Rouge e stampare Hello, World!.

It is the Clojure language on Ruby identified by the canonical entry .rg. The driver calls Rouge.repl and the parser/evaluatore authentic currency puts and str.

## Toolchain and reproduction

Original Rouge from the vic/rouge repository, Ruby3.2.3

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
ruby -I /path/to/rouge/lib run.rb hello.rg
```

## Expected result and status

Hello, World! su stdout.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://github.com/vic/rouge

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.rg` | [hello.rg](hello.rg) verified |
