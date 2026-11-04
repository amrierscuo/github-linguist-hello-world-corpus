# #056 BQN

Voce canonica: `BQN`, tipo `programming`, `language_id: 330386870`.

Concatenate three BQN strings and write Hello, World! using the •Out system.

## Toolchain and reproduction

Official CBQN C implementation locally built, c893d3e7828899a50150df03ad33c9052fa51d3c. Test environment: **Ubuntu 24.04 WSL2/Linux x86_64**.

CBQN was compiled from the official repository at commit c893d3e7828899a50150df03ad33c9052fa51d3c. Local Linux build: make REPLXX=0 FFI=0 -j2. The program does not require REPL editor or FFI features.

Comando/procedura from the example directory:

```text
BQN hello.bqn
```

Exit 0; stdout Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The verification uses the true CBQN interpreter. The log contains commit and SHA-256 of the track, as well as the SHA-256 of the BQN source. The concatenation  ⁇  and the assignment ← are syntax BQN.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain and SHA-256 of artifacts. `path_normalization` describes the replacements of artifacts.
machine paths; source bytes remain those identified by checksums.
If the log only records the availability of the tools, no parsing or runtime is attested.
Tools, dependencies and verification products remain in the work directory.

## Primary sources

- [https://mlochbaum.github.io/BQN/doc/quick.html](https://mlochbaum.github.io/BQN/doc/quick.html)
- [https://github.com/dzaima/CBQN](https://github.com/dzaima/CBQN)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bqn` | [hello.bqn](hello.bqn) verified |
