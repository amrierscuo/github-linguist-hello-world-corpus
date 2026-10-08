# #410 MLIR

Verificare MLIR in LLVM dialect, tradurlo in LLVM IR e produrre un eseguibile che chiama puts.

Tipo canonico `programming`, language_id `448253929`.

Toolchain prevista: LLVM/MLIR tools mlir-opt, mlir-translate e clang.

Dalla cartella dell’esempio:

```sh
mlir-opt hello.mlir -o build/checked.mlir
mlir-translate --mlir-to-llvmir build/checked.mlir -o build/hello.ll
lli build/hello.ll
```

Risultato atteso: stdout Hello, World! e LF; exit 0.

La stringa contiene il terminatore NUL richiesto da puts. Parsing e verifica MLIR sono distinti da traduzione, linking ed esecuzione.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Ubuntu LLVM/MLIR 18.1.3 (mlir-opt, mlir-translate, lli). [Log](verification/result.json). 

Fonti:

- [MLIR — LLVM dialect](https://mlir.llvm.org/docs/Dialects/LLVM/)

Verifica effettiva: parsing/verifica del dialect LLVM, traduzione in LLVM IR ed esecuzione JIT con lli. Il saluto proviene dalla chiamata puts nel modulo tradotto.

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mlir` | [hello.mlir](hello.mlir) verificato |
