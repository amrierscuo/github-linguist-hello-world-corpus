# #410 MLIR

Check MLIR in LLVM dialect, translate it into LLVM IR and produce an executable that calls puts.

Canonical type `programming`, language_id `448253929`.

Suggested toolchain: LLVM/MLIR tools mlir-opt, mlir-translate and clang.

From the example directory:

```sh
mlir-opt hello.mlir -o build/checked.mlir
mlir-translate --mlir-to-llvmir build/checked.mlir -o build/hello.ll
lli build/hello.ll
```

Expected result: stdout Hello, World! and LF; exit 0.

The string contains the NUL terminator required by puts. Parsing and MLIR verification are distinguished by translation, linking and execution.

Recorded status: syntax verified; behavior verified. Toolchain: Ubuntu LLVM/MLIR 18.1.3 (mlir-opt, mlir-translate, lli). [Log](verification/result.json).

Sources:

- [MLIR — LLVM dialect](https://mlir.llvm.org/docs/Dialects/LLVM/)

Effective verification: parsing/verifica of the dialect LLVM, translation into LLVM IR and JIT execution with lli.

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mlir` | [hello.mlir](hello.mlir) verified |
