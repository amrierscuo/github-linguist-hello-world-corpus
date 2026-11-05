# Native checks to reach 546 verified samples: November 5, 2026

The batch used console or headless tools and did not invoke .NET. Verification applies to the exact inputs and scope in each receipt. The prior report remains available.

## Main sample checks

- **#105 Cairo**: Syntax and behavior verified. Pinned Scarb compiled the unchanged Cairo executable project and cairo_execute ran it, producing the exact greeting line. No Starknet contract, wallet or network transaction was involved. [Evidence](../examples/%23105%20Cairo/verification/native_20261105_target546_main.json).
- **#218 FreeBASIC**: Syntax and behavior verified. Authentic FreeBASIC compiled the unchanged main and original .bi include consumer; both native executables printed exactly Hello, World!. Required compatibility libraries were extracted locally without system installation. [Evidence](../examples/%23218%20FreeBASIC/verification/native_20261105_target546_main.json).
- **#268 Grammatical Framework**: Syntax and behavior verified. The native GF compiler accepted the exact abstract and concrete grammar, generated the PGF, and the GF runtime linearized the Hello tree to exactly Hello, World!. No RGL dependency or GUI. [Evidence](../examples/%23268%20Grammatical%20Framework/verification/native_20261105_target546_main.json).
- **#291 Harbour**: Syntax and behavior verified. The genuine native Harbour hbmk2 script mode, built from the official source, parsed and executed the unchanged .hb script and emitted the exact greeting and LF. No UI, database or service was used. [Evidence](../examples/%23291%20Harbour/verification/native_20261105_target546_main.json).
- **#316 Ioke**: Syntax and behavior verified. The official Ioke JVM implementation parsed and executed the unchanged Ioke message-send source and printed exactly Hello, World! with LF. No Io substitution, CLR backend or GUI was used. [Evidence](../examples/%23316%20Ioke/verification/native_20261105_target546_main.json).
- **#437 Mirah**: Syntax and behavior verified. The original Mirah source was compiled by Mirah and its generated JVM class printed exactly Hello, World! plus LF. No Ruby substitution or GUI was used. [Evidence](../examples/%23437%20Mirah/verification/native_20261105_target546_main.json).
- **#617 Ring**: Syntax and behavior verified. The official Ring1.27 console VM compiled the unchanged source and executed see/concatenation, emitting the exact greeting and LF. Only ANSI-C language/VM/standard-function sources were built; no GUI extensions, IDE or system installation. [Evidence](../examples/%23617%20Ring/verification/native_20261105_target546_main.json).
- **#705 TXL**: Syntax and behavior verified. After the minimal construct-type correction, native OpenTXL parsed the grammar and rewrite function and transformed the original input.txt into exactly the quoted Hello, World! string-literal token. The output is a transformed program token, not an unquoted console print. The original compiler failure is retained. [Evidence](../examples/%23705%20TXL/verification/native_20261105_target546_main.json).
- **#722 Toit**: Syntax and behavior verified. The official native Toit2.0 compiler/runtime compiled and ran the exact original main/print source on Linux and emitted exactly the greeting and LF. No embedded device, cloud service or GUI was used. [Evidence](../examples/%23722%20Toit/verification/native_20261105_target546_main.json).
- **#738 Untyped Plutus Core**: Syntax and behavior verified. The maintained Aiken native UPLC parser and CEK evaluator loaded the exact original program and evaluated it to (con string "Hello, World!") with recorded positive CPU/memory budget usage. This verifies the pure UPLC constant only; no blockchain, wallet, deployment or transaction was involved. [Evidence](../examples/%23738%20Untyped%20Plutus%20Core/verification/native_20261105_target546_main.json).

## Extension checks

- **#105 Cairo**, `.cairo`: Syntax and behavior verified. [Evidence](../examples/%23105%20Cairo/verification/native_20261105_target546_main.json).
- **#218 FreeBASIC**, `.bas`, `.bi`: Syntax and behavior verified. [Evidence](../examples/%23218%20FreeBASIC/verification/native_20261105_target546_main.json).
- **#268 Grammatical Framework**, `.gf`: Syntax and behavior verified. [Evidence](../examples/%23268%20Grammatical%20Framework/verification/native_20261105_target546_main.json).
- **#291 Harbour**, `.hb`: Syntax and behavior verified. [Evidence](../examples/%23291%20Harbour/verification/native_20261105_target546_main.json).
- **#316 Ioke**, `.ik`: Syntax and behavior verified. [Evidence](../examples/%23316%20Ioke/verification/native_20261105_target546_main.json).
- **#437 Mirah**, `.mirah`: Syntax and behavior verified. [Evidence](../examples/%23437%20Mirah/verification/native_20261105_target546_main.json).
- **#617 Ring**, `.ring`: Syntax and behavior verified. [Evidence](../examples/%23617%20Ring/verification/native_20261105_target546_main.json).
- **#705 TXL**, `.txl`: Syntax and behavior verified. [Evidence](../examples/%23705%20TXL/verification/native_20261105_target546_main.json).
- **#722 Toit**, `.toit`: Syntax and behavior verified. [Evidence](../examples/%23722%20Toit/verification/native_20261105_target546_main.json).
- **#738 Untyped Plutus Core**, `.uplc`: Syntax and behavior verified. [Evidence](../examples/%23738%20Untyped%20Plutus%20Core/verification/native_20261105_target546_main.json).

Main samples: 573/836 syntax and 546/836 behavior verified; 290 behavior checks remain pending.
Language and extension pairs: 791/1749 syntax and 717/1749 behavior verified.
