# #579 Quartus Simulation IP

## Verified on November 18, 2026

Tcl evaluated the unchanged SIP with a fixture for Quartus assignment collection. The resolved unchanged simulation source ran in Icarus Verilog and printed the greeting.

Run `tclsh load_sip.tcl; iverilog -o hello.vvp <SIP-assigned input>; vvp hello.vvp`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Referee a simulation testbench in a SIP Quartus file.

## Toolchain

Quartus Prime project Tcl; simulator Verilog

## Procedure

Import hello.sip into the Quartus project and simulate hello_tb.v with the compatible simulator.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

MISC_FILE/file join/quartus(sip_path) follow the canonical sample format; the original testbench is the consumer of the reference.

Remaining requirements:
- Quartus project reader e simulatore non predisposti.

## Primary sources

- [https://www.intel.com/content/www/us/en/docs/programmable/683609/23-1/simulation-files.html](https://www.intel.com/content/www/us/en/docs/programmable/683609/23-1/simulation-files.html)
- [https://github.com/github-linguist/linguist/tree/main/samples/Quartus%20Simulation%20IP](https://github.com/github-linguist/linguist/tree/main/samples/Quartus%20Simulation%20IP)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sip` | [hello.sip](hello.sip) Syntax and behavior verified |

</details>
