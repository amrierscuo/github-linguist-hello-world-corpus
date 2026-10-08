# #314 Inno Setup

Mostrare Hello, World! quando inizializza il wizard di un installer Inno Setup.

## Toolchain

Inno Setup ISCC; versione da registrare

## Comandi e procedura

ISCC /O"build" hello.iss; avviare build/hello-world-setup.exe in ambiente di prova e controllare il MsgBox

## Risultato atteso

Compilazione accettata; MsgBox di InitializeWizard contiene il saluto.

## Stato

Sintassi e semantica in attesa.

La procedura Pascal è un callback originale di Inno Setup. Non sono inclusi file da installare; la prova GUI resta da fare in un ambiente dedicato. Non è stato lanciato alcun installer.

Requisiti residui:
- ISCC non presente; compilazione script e callback wizard non eseguiti.

## Fonti primarie

- [https://jrsoftware.org/ishelp/topic_setupsection.htm](https://jrsoftware.org/ishelp/topic_setupsection.htm)
- [https://jrsoftware.org/ishelp/topic_scriptevents.htm](https://jrsoftware.org/ishelp/topic_scriptevents.htm)
- [https://jrsoftware.org/ishelp/topic_isxfunc_msgbox.htm](https://jrsoftware.org/ishelp/topic_isxfunc_msgbox.htm)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.iss` | [hello.iss](hello.iss), [driver.iss](variants/isl-41200207/driver.iss) creato, verifiche pendenti |
| `.isl` | [hello.isl](variants/isl-41200207/hello.isl) creato, verifiche pendenti |
