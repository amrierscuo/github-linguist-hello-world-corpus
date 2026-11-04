# 0807: Zig: `.zig.zon`

Manifest Zig Object Notation of local package without invented dipendenze/hash.

Provenience: original example written for the role of this suffix.

Artefatto principale: `build.zig.zon`.

Control provided, from the folder of the variant:

```text
${WORKSPACE}\work\tools_801_820\zig\zig-x86_64-windows-0.15.2\zig.exe version
${WORKSPACE}\work\tools_801_820\zig\zig-x86_64-windows-0.15.2\zig.exe fmt build.zig.zon build.zig hello.zig
${WORKSPACE}\work\tools_801_820\zig\zig-x86_64-windows-0.15.2\zig.exe build --prefix ${WORKSPACE}\work\verify_extensions_561_836\807_af1980a8\installed
${WORKSPACE}\work\verify_extensions_561_836\807_af1980a8\installed\bin\corpus-greeting.exe
```

Expected result: accepted poster and original program produces Hello, World!.

Status: created; syntax verified; behavior verified.

Toolchain osservata: Zig 0.15.2.

Real ambition: Manifest ZON original with fingerprint assigned by zig init; zig build accepts the local package and the program produces Hello, World! on stderr.

Log: `verification/result.json`; SHA-256 of each sorgente/supporto of the variant, commands, exit code and actual output. Build/cache remain under `work/verify_extensions_561_836`.

Primary sources:

- [https://raw.githubusercontent.com/ziglang/zig/0.15.2/lib/init/build.zig.zon](https://raw.githubusercontent.com/ziglang/zig/0.15.2/lib/init/build.zig.zon)
