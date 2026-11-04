# #073 Bluespec

Canonical entry from the corpus's `reference/languages.yml`. The reference and its order remain unchanged. The source was written for this example.

## Goal

Simulate a Bluespec SystemVerilog rule that prints Hello, World! and ends.

Hello.bsv uses the Bluespec SystemVerilog dialect. The rule invokes $display and $finish; the test involves Bluesim simulation, not implementation on FPGA. Binaries and processing files remain out of the corpus.

## Toolchain and reproduction

B-Lang BSC 2026.07.1 for Ubuntu 24.04; GNU C++; Tcl 8.6.14 isolated

Command from the example folder, with the toolchain indicated available in the PATH. Run the build in a temporary copy to keep the generated files out of the corpus.

```text
bsc -u -sim -g mkHello Hello.bsv
bsc -sim -e mkHello -o hello
```

```text
./hello
```

## Expected result and status

stdout esatto Hello, World! seguito da newline; simulazione exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records actual commands, versioni/provenienza of the toolchain, output codes, stdout/stderr and SHA-256 of the proven sources.

## Primary sources

- https://bluespec.dev/bsv-reference/modules-and-interfaces--and-their-instances-rules-in-module-definitions.html
- https://github.com/B-Lang-org/bsc/releases/tag/2026.07.1

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bsv` | [Hello.bsv](Hello.bsv) verified |
