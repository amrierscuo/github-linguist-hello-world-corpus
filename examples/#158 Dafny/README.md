# #158 Dafny

The canonical entry and order come from the corpus's `reference/languages.yml`. Sources and fixtures are original; any dumps or bundles come from the stated tools.

## Goal

Demonstrate string and length of greeting in Dafny, fill in JavaScript and execute it.

Le assert dimostrano valore e lunghezza 13. La prova SMT precede la compilazione/esecuzione del backend JavaScript. Il log distingue esito del verificatore e output runtime; il backend usa bignumber.js isolato tramite NODE_PATH. Il runner effettivo carica DafnyDriver.dll con dotnet.

## Toolchain and reproduction

Dafny 3.13.1.50302; .NET 6.0.36; Z3 5.1.0; Node.js 22.20.0; bignumber.js

Commands in the example folder with the toolchain available in PATH. Use a temporary copy: databases, objects, audio and other test outputs do not belong to the corpus.

```text
dafny /compile:0 /proverOpt:PROVER_PATH=<z3> hello.dfy
```

```text
dafny /compileTarget:js /compile:3 /proverOpt:PROVER_PATH=<z3> hello.dfy
```

## Expected result and status

1 verified, 0 errors; the compiled program emits Hello, World! and newline.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records versions and provenance, SHA-256 of the source, actual commands, exit, stdout and stderr normalized.

## Primary sources

- https://dafny.org/dafny/DafnyRef/DafnyRef
- https://github.com/dafny-lang/dafny

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.dfy` | [hello.dfy](hello.dfy) verified |
