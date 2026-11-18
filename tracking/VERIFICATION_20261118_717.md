# Verification of 717 main examples on November 18, 2026

This batch recorded 10 new behavior checks. The corpus contains 726 main examples with verified syntax and 717 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

The [previous checkpoint](VERIFICATION_20261118_707.md) records the earlier checks in this session.

- **#035 Apollo Guidance Computer**. The official assembler and native Block II emulation core processed the unchanged code. Reading its A register confirmed the intended octal greeting byte after executing the original instructions. The same evidence covers `.agc`. [Evidence](../examples/%23035%20Apollo%20Guidance%20Computer/verification/native_20261118_wave736_main.json).
- **#108 Cangjie**. The published compiler built the unchanged Cangjie program and the resulting console application printed the exact greeting. The same evidence covers `.cj`. [Evidence](../examples/%23108%20Cangjie/verification/native_20261118_wave736_main.json).
- **#173 E**. The archived E-on-Java interpreter evaluated the original console sample and emitted the exact greeting. The same evidence covers `.e`. [Evidence](../examples/%23173%20E/verification/native_20261118_wave736_main.json).
- **#273 Groovy Server Pages**. The maintained Apache Grails GSP engine rendered the unchanged original template with its model binding. The emitted page contains the exact greeting. The same evidence covers `.gsp`. [Evidence](../examples/%23273%20Groovy%20Server%20Pages/verification/native_20261118_wave736_main.json).
- **#397 Logos**. The original Logos preprocessor emitted the constructor. The scratch host invoked its unchanged body after GNUstep initialization and captured the exact NSLog greeting. The same evidence covers `.xm`. [Evidence](../examples/%23397%20Logos/verification/native_20261118_wave736_main.json).
- **#554 Pro*C**. The compatible embedded-SQL precompiler translated the unmodified source and preserved its declared C host variable. Running the generated executable printed the exact greeting. The same evidence covers `.pc`. [Evidence](../examples/%23554%20Pro%E2%88%97C/verification/native_20261118_wave736_main.json).
- **#637 SQLPL**. The compatible SQL/PSM engine created the procedure and invoked it through JDBC. The registered OUT parameter returned the exact greeting. The same evidence covers `.db2`. [Evidence](../examples/%23637%20SQLPL/verification/native_20261118_wave736_main.json).
- **#676 SourcePawn**. The released compiler compiled the original plugin. The published compatible VM executed the actual SMX OnPluginStart entry point and emitted the exact greeting. [Evidence](../examples/%23676%20SourcePawn/verification/native_20261118_wave736_main.json).
- **#770 Whiley**. The official compiler generated WYIL from the unmodified original. Its interpreter evaluated the greeting function and returned the exact thirteen-byte greeting. The same evidence covers `.whiley`. [Evidence](../examples/%23770%20Whiley/verification/native_20261118_wave736_main.json).
- **#777 World of Warcraft Addon Data**. The compatible addon loader opened the exact original TOC, selected its referenced Lua file and executed it. Its chat hook received the exact greeting. The same evidence covers `.toc`. [Evidence](../examples/%23777%20World%20of%20Warcraft%20Addon%20Data/verification/native_20261118_wave736_main.json).

869 of 1,749 language and extension pairs now have verified behavior.
