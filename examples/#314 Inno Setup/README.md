# #314 Inno Setup

Show Hello, World! when it initializes the wizard of an Inno Setup installer.

## Toolchain

Inno Setup ISCC; versione da registrare

## Commands and procedure

ISCC /O "build" hello.iss; start build/hello-world-setup.exe in test environment and check the MsgBox

## Expected result

Accepted compilation; MsgBox of InitializeWizard contains greetings.

## Status

Syntax and behavioral verification pending.

The Pascal procedure is an original callback of Inno Setup. There are no files to install; the GUI test remains to be done in a dedicated environment. No installer has been launched.

Remaining requirements:
- ISCC not present; compilation script and callback wizard not executed.

## Primary sources

- [https://jrsoftware.org/ishelp/topic_setupsection.htm](https://jrsoftware.org/ishelp/topic_setupsection.htm)
- [https://jrsoftware.org/ishelp/topic_scriptevents.htm](https://jrsoftware.org/ishelp/topic_scriptevents.htm)
- [https://jrsoftware.org/ishelp/topic_isxfunc_msgbox.htm](https://jrsoftware.org/ishelp/topic_isxfunc_msgbox.htm)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.iss` | [hello.iss](hello.iss), [driver.iss](variants/isl-41200207/driver.iss) created; verification pending |
| `.isl` | [hello.isl](variants/isl-41200207/hello.isl) created; verification pending |
