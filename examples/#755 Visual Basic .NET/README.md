# #755 Visual Basic .NET

Fill out Visual Basic .NET and print your greeting.

Canonical type `programming`, language_id `389`.

Suggested toolchain: Microsoft .NET Framework vbc 4.8 + CLR.

From the example directory:

```sh
mkdir -p build
vbc /nologo /target:exe /vbruntime- '/define:_MYTYPE="Empty"' /out:build/Hello.exe Hello.vb
build/Hello.exe
```

Expected result: CLR press Hello, World! and newline.

The class uses a Shared Main method without the need for UI.

Recorded status: syntax verified; behavior verified. Toolchain: Microsoft .NET Framework vbc 4.8 + CLR. [Log](verification/result.json).

Sources:

- [Visual Basic main](https://learn.microsoft.com/en-us/dotnet/visual-basic/programming-guide/program-structure/main-procedure)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.vb` | [Hello.vb](Hello.vb) verified |
| `.vbhtml` | [hello.vbhtml](variants/vbhtml-d3316377/hello.vbhtml) created; verification pending |
