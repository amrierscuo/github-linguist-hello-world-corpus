# #015 ASL

This entry indicates **ACPI Source Language**. `hello.asl` defines a SSDT table
with the `HWLD` method, which writes `Hello World` in the Debug object and returns the
The test uses the ACPICA interpreter in user space.

Toolchain verified: ACPICA `iasl` e `acpiexec`, versione **20250807**, Windows x64.
The tracks are available in [release ufficiale ACPICA](https://github.com/open-acpica/acpica/releases/tag/20250807)
( `iasl-win-20250807.zip` archive) and are not included in the corpus.

From the example folder, with ACPICA executables in PATH:

```powershell
iasl hello.asl
acpiexec -b "execute HWLD" hello.aml
```

To automatically verify the result, producing artifacts in
a new folder external to the example:

```powershell
powershell -NoProfile -File .\verify.ps1 -AcpicaDirectory C:\tools\acpica -BuildDirectory C:\temp\asl-check
```

Expected result: compilation without errors; the user log contains
`ACPI Debug: "Hello World"` e `[String] Length 0B = "Hello World"`.
syntax and behavior verified: **sì**, vedere `verification.log`.
The control concerns this method in the ACPICA simulator; it is not a test
integration into the firmware of a machine.

Riferimento primario: [ACPI Source Language Reference, UEFI Forum](https://uefi.org/htmlspecs/ACPI_Spec_6_4_html/19_ASL_Reference/ACPI_Source_Language_Reference.html).

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.asl` | [hello.asl](hello.asl) verified |
| `.dsl` | [hello.dsl](variants/ext-dsl-2e64736c/hello.dsl) created; verification pending |
