# #102 Cabal Config

The official Cabal Setup driver configured and built the original package. Its executable printed Hello, World!

Canonical type: `data`. Linguist language ID: `677095381`.

## Recorded verification

**Syntax and behavior verified** on November 4, 2026 with Cabal 3.8.1.0 and GHC 9.4.7.

[Recorded commands, outputs and hashes](verification/native_20261104_receipt.json).

## Reproduce the check

Copy the package, `src/Main.hs` and `verification/Setup.hs` into a scratch directory. With GHC and its Cabal library available, run:

```sh
runghc Setup.hs configure --user --builddir=dist
runghc Setup.hs build --builddir=dist
./dist/build/hello-world
```

This check used the Cabal library Setup driver. It did not exercise cabal-install or cabal.project.

## Primary sources


## Extension coverage

| Extension | Files | Status |
| --- | --- | --- |
| `.cabal` | [hello-world.cabal](hello-world.cabal) | Syntax and behavior verified |
