# 0807 — Zig — `.zig.zon`

Manifest Zig Object Notation di package locale senza dipendenze/hash inventati.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `build.zig.zon`.

Controllo previsto, dalla cartella della variante:

```text
${WORKSPACE}\work\tools_801_820\zig\zig-x86_64-windows-0.15.2\zig.exe version
${WORKSPACE}\work\tools_801_820\zig\zig-x86_64-windows-0.15.2\zig.exe fmt build.zig.zon build.zig hello.zig
${WORKSPACE}\work\tools_801_820\zig\zig-x86_64-windows-0.15.2\zig.exe build --prefix ${WORKSPACE}\work\verify_extensions_561_836\807_af1980a8\installed
${WORKSPACE}\work\verify_extensions_561_836\807_af1980a8\installed\bin\corpus-greeting.exe
```

Risultato atteso: manifest accettato e programma originale produce Hello, World!.

Stato: creato; sintassi verificata; semantica verificata.

Toolchain osservata: Zig 0.15.2.

Ambito reale: Manifest ZON originale con fingerprint assegnato da zig init; zig build accetta il package locale e il programma produce Hello, World! su stderr.

Log: `verification/result.json`; SHA-256 di ogni sorgente/supporto della variante, comandi, exit code e output effettivi. Build/cache restano sotto `work/verify_extensions_561_836`.

Fonti primarie:

- [https://raw.githubusercontent.com/ziglang/zig/0.15.2/lib/init/build.zig.zon](https://raw.githubusercontent.com/ziglang/zig/0.15.2/lib/init/build.zig.zon)
