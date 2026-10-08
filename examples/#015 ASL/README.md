# #015 ASL

Questa voce indica **ACPI Source Language**. `hello.asl` definisce una tabella SSDT
con il metodo `HWLD`, che scrive `Hello World` nell'oggetto Debug e restituisce la
stessa stringa. Il test usa l'interprete ACPICA in spazio utente.

Toolchain verificata: ACPICA `iasl` e `acpiexec`, versione **20250807**, Windows x64.
I binari sono disponibili nella [release ufficiale ACPICA](https://github.com/open-acpica/acpica/releases/tag/20250807)
(archivio `iasl-win-20250807.zip`) e non sono inclusi nel corpus.

Dalla cartella dell'esempio, con gli eseguibili ACPICA nel PATH:

```powershell
iasl hello.asl
acpiexec -b "execute HWLD" hello.aml
```

Per verificare anche automaticamente il risultato, producendo gli artefatti in
una cartella nuova esterna all'esempio:

```powershell
powershell -NoProfile -File .\verify.ps1 -AcpicaDirectory C:\tools\acpica -BuildDirectory C:\temp\asl-check
```

Risultato atteso: compilazione senza errori; il log dell'interprete contiene
`ACPI Debug: "Hello World"` e `[String] Length 0B = "Hello World"`.
Sintassi e semantica verificate: **sì**, vedere `verification.log`.
Il controllo riguarda questo metodo nel simulatore ACPICA; non è una prova
di integrazione nel firmware di una macchina.

Riferimento primario: [ACPI Source Language Reference, UEFI Forum](https://uefi.org/htmlspecs/ACPI_Spec_6_4_html/19_ASL_Reference/ACPI_Source_Language_Reference.html).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.asl` | [hello.asl](hello.asl) verificato |
| `.dsl` | [hello.dsl](variants/ext-dsl-2e64736c/hello.dsl) creato, verifiche pendenti |
