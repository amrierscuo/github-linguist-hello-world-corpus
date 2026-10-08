# #756 Visual Basic 6.0

Compilare un progetto Visual Basic 6 e mostrare il saluto con MsgBox.

Tipo canonico `programming`, language_id `679594952`.

Toolchain prevista: Microsoft Visual Basic 6 compiler/runtime.

Dalla cartella dell’esempio:

```sh
VB6.EXE /make hello.vbp
```

Risultato atteso: progetto compilato; finestra MsgBox Hello, World!.

Non viene sostituito con VB.NET o VBScript.

Stato iniziale: creato; sintassi e semantica in attesa. Visual Basic 6 compiler non disponibile.

Fonti:

- [VB6 support](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-basic-6/visual-basic-6-support-policy)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bas` | [hello.bas](hello.bas) creato, verifiche pendenti |
| `.cls` | [hello.cls](variants/cls-699ea095/hello.cls) creato, verifiche pendenti |
| `.ctl` | [hello.ctl](variants/ctl-04279ee3/hello.ctl) creato, verifiche pendenti |
| `.Dsr` | artefatto da generare Designer DataReport VB6: occorre un export originale dell’IDE e il relativo stream designer .dsx. Non viene inventata una serializzazione OLE. |
| `.frm` | [hello.frm](variants/frm-f409e81b/hello.frm) creato, verifiche pendenti |
