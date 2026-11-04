# #742 VBScript

Run VBScript with the Windows host script console.

Canonical type `programming`, language_id `408016005`.

Suggested toolchain: Windows cscript.exe and VBScript engine.

From the example directory:

```sh
cscript //nologo hello.vbs
```

Expected result: stdout Hello, World! and newline.

cscript is used in console mode, without dialogues.

Recorded status: syntax verified; behavior verified. Toolchain: Windows cscript console host + original VBScript engine. [Log](verification/result.json).

Sources:

- [Windows Script Host](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/legacy/9bbdkx3k(v=vs.85))

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.vbs` | [hello.vbs](hello.vbs) verified |
