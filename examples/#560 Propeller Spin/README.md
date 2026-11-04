# #560 Propeller Spin

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Fill Propeller Spin and make available the DAT Hello, World! string to main.

DAT definisce13byte ASCII e il terminatore NUL; PUB main restituisce il puntatore alla stringa. Il compiler autentico genera un binario44byte. L’esecuzione del target e la lettura del dato non vengono attribuite alla sola compilazione.

## Toolchain and reproduction

OpenSpin1.00.81 originale Parallax; costruito con GCC/G++

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
openspin -b -o hello.binary hello.spin
```

```text
Caricare/eseguire hello.binary su un runtime Propeller appropriato.
```

## Expected result and status

Accepted compilation; main returns the address of Hello, World! NUL.

Artifact created: yes. syntax verified: yes. behavior verified: no.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

Impedimenti: Runtime/emulatore Propeller non preparato; semantica pendente.

## Primary sources

- https://github.com/parallaxinc/OpenSpin

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.spin` | [hello.spin](hello.spin) syntax verified |
