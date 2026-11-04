# #076 Boogie

Canonical entry from the corpus's `reference/languages.yml`. The reference and its order remain unchanged. The source was written for this example.

## Goal

Demonstrate that Greeting returns 13 length and 13 ASCII string Hello, World! codes.

Boogie is a verification language: the behavior here is the proof of post-conditions, not a consul print. The program assigns the length and every element of the map; Z3 demonstrates all post-conditions. The actual runner invokes BoogieDriver.dll with dotnet and the path of the explicit solver.

## Toolchain and reproduction

Boogie 2.15.9.0, .NET 6.0.36, Z3 5.1.0 64-bit

Command from the example folder, with the toolchain indicated available in the PATH. Run the build in a temporary copy to keep the generated files out of the corpus.

```text
boogie /noVerify hello.bpl
boogie /proverOpt:PROVER_PATH=<z3> hello.bpl
```

## Expected result and status

Parsing and typecheck without errors; Boogie: 1 verified, 0 errors.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records actual commands, versioni/provenienza of the toolchain, output codes, stdout/stderr and SHA-256 of the proven sources.

## Primary sources

- https://github.com/boogie-org/boogie
- https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/krml178.pdf

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bpl` | [hello.bpl](hello.bpl) verified |
