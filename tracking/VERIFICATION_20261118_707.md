# Verification of 707 main examples on November 18, 2026

This batch recorded 14 new behavior checks. The corpus contains 718 main examples with verified syntax and 707 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

The [previous checkpoint](VERIFICATION_20261118_693.md) records the earlier checks in this session.

- **#034 Apex**. The compatible interpreter ran the exact anonymous Apex statements directly as anonymous Apex. System.assertEquals passed and the runtime executed the original System.debug call with the exact greeting. The same evidence covers `.apex`. [Evidence](../examples/%23034%20Apex/verification/native_20261118_wave736_main.json).
- **#082 BuildStream**. The official BuildStream project built the unchanged import element. Its artifact checkout materialized a file with the exact expected greeting and newline. The same evidence covers `.bst`. [Evidence](../examples/%23082%20BuildStream/verification/native_20261118_wave736_main.json).
- **#121 Classic ASP**. The original embedded VBScript ran in the Microsoft script host using a standalone Classic ASP Response fixture. A private HTTP request returned status 200, the original content type and charset, and the exact greeting. The same evidence covers `.asp`. [Evidence](../examples/%23121%20Classic%20ASP/verification/native_20261118_wave736_main.json).
- **#176 ECL**. The official native ECL compiler compiled the original workunit. Running it returned the expected scalar greeting. The same evidence covers `.ecl`. [Evidence](../examples/%23176%20ECL/verification/native_20261118_wave736_main.json).
- **#251 Glimmer JS**. The content-tag compiler and host transpiler processed the unchanged original source. A standalone Glimmer runtime mounted its compiled template and the heading contained the exact greeting. The same evidence covers `.gjs`. [Evidence](../examples/%23251%20Glimmer%20JS/verification/native_20261118_wave736_main.json).
- **#252 Glimmer TS**. The content-tag compiler and host transpiler processed the unchanged original source. A standalone Glimmer runtime mounted its compiled template and the heading contained the exact greeting. The same evidence covers `.gts`. [Evidence](../examples/%23252%20Glimmer%20TS/verification/native_20261118_wave736_main.json).
- **#295 HiveQL**. The official Apache Hive SQL driver evaluated the original SELECT against a private local session and returned the exact scalar row. [Evidence](../examples/%23295%20HiveQL/verification/native_20261118_wave736_main.json).
- **#317 Isabelle**. Isabelle checked the original ROOT session and theorem. The standard session log recorded evaluation of the original greeting value. The same evidence covers `.thy`. [Evidence](../examples/%23317%20Isabelle/verification/native_20261118_wave736_main.json).
- **#318 Isabelle ROOT**. Isabelle checked the original ROOT session and theorem. The standard session log recorded evaluation of the original greeting value. [Evidence](../examples/%23318%20Isabelle%20ROOT/verification/native_20261118_wave736_main.json).
- **#365 Kusto**. ClickHouse’s KQL-compatible runtime evaluated the exact original query and returned the greeting under its declared column. The same evidence covers `.kql`. [Evidence](../examples/%23365%20Kusto/verification/native_20261118_wave736_main.json).
- **#621 Roc**. The published Roc nightly ran the sample with the verified CLI platform and executed its greeting action and emitted the greeting. The same evidence covers `.roc`. [Evidence](../examples/%23621%20Roc/verification/native_20261118_wave736_main.json).
- **#741 VBA**. The Microsoft VBScript interpreter executed the unchanged VBA routine in the shared language subset. A console fixture for the VBA Debug object received the exact Debug.Print argument. The same evidence covers `.bas`. [Evidence](../examples/%23741%20VBA/verification/native_20261118_wave736_main.json).
- **#756 Visual Basic 6.0**. The published compatible tool read the original VBP and BAS, compiled the project and invoked its declared Sub Main. The virtual machine passed the exact greeting to the headless MsgBox callback. The same evidence covers `.bas`. [Evidence](../examples/%23756%20Visual%20Basic%206.0/verification/native_20261118_wave736_main.json).
- **#829 q**. The published PeachQ implementation executed the unchanged q script. Its console printed the exact greeting. The same evidence covers `.q`. [Evidence](../examples/%23829%20q/verification/native_20261118_wave736_main.json).

860 of 1,749 language and extension pairs now have verified behavior.
