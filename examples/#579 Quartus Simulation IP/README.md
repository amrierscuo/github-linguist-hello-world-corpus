# #579 Quartus Simulation IP

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
| `.sip` | [hello.sip](hello.sip) created; verification pending |
