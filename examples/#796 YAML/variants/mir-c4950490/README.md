# 0796 — `.mir`

LLVM MIR x86-64 generato realmente da llc18 dopo finalize-isel; Machine IR originale con wrapper LLVM IR. Il sorgente .ll è incluso per riproducibilità.

Provenienza: produttore/serializzatore originale eseguito, come registrato nel log.

Artefatto principale: `hello.mir`.

Controllo previsto:

```text
${WORKSPACE_WSL}/work/tools_361_380/ubuntu/usr/lib/llvm-18/bin/llc --version
${WORKSPACE_WSL}/work/tools_361_380/ubuntu/usr/lib/llvm-18/bin/llc -stop-after=finalize-isel greeting.ll -o hello.mir
${WORKSPACE_WSL}/work/tools_361_380/ubuntu/usr/lib/llvm-18/bin/llc -run-pass=none hello.mir -o parsed.mir
${WORKSPACE_WSL}/work/tools_361_380/ubuntu/usr/lib/llvm-18/bin/llc hello.mir -o hello.s
gcc -no-pie hello.s -o hello
./hello
```

Risultato atteso: MIR accettato da llc; programma linkato stampa Hello, World!.

Stato: creato; sintassi verificata; semantica verificata.

Toolchain osservata: Ubuntu LLVM version 18.1.3.

Ambito reale: llc originale rilegge il MIR generato, genera assembly reale, GCC linka e il processo eseguito stampa il saluto esatto.

Log: `verification/result.json`; SHA-256 di ogni sorgente/supporto della variante, comandi, exit code e output effettivi. Build/cache restano sotto `work/verify_extensions_561_836`.

Fonti primarie:

- [https://llvm.org/docs/MIRLangRef.html](https://llvm.org/docs/MIRLangRef.html)
