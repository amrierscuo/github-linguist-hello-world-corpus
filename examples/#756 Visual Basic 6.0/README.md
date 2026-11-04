# #756 Visual Basic 6.0

Fill out a Visual Basic 6 project and show greeting with MsgBox.

Canonical type `programming`, language_id `679594952`.

Suggested toolchain: Microsoft Visual Basic 6 compiler/runtime.

From the example directory:

```sh
VB6.EXE /make hello.vbp
```

Expected result: compiled project; window MsgBox Hello, World!.

It is not replaced with VB.NET or VBScript.

Initial state: created; syntax and behavioral verification pending. Visual Basic 6 compiler unavailable.

Sources:

- [VB6 support](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-basic-6/visual-basic-6-support-policy)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bas` | [hello.bas](hello.bas) created; verification pending |
| `.cls` | [hello.cls](variants/cls-699ea095/hello.cls) created; verification pending |
| `.ctl` | [hello.ctl](variants/ctl-04279ee3/hello.ctl) created; verification pending |
| `.Dsr` | created by Designer DataReport VB6: an original export of IDE and its stream designer .dsx. is not invented a OLE serialization. |
| `.frm` | [hello.frm](variants/frm-f409e81b/hello.frm) created; verification pending |
