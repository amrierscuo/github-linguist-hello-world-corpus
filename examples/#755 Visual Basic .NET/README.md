# #755 Visual Basic .NET

Compilare Visual Basic .NET e stampare il saluto.

Tipo canonico `programming`, language_id `389`.

Toolchain prevista: Microsoft .NET Framework vbc 4.8 + CLR.

Dalla cartella dell’esempio:

```sh
mkdir -p build
vbc /nologo /target:exe /vbruntime- '/define:_MYTYPE="Empty"' /out:build/Hello.exe Hello.vb
build/Hello.exe
```

Risultato atteso: programma CLR stampa Hello, World! e newline.

La classe usa un metodo Shared Main senza necessità di UI.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Microsoft .NET Framework vbc 4.8 + CLR. [Log](verification/result.json). 

Fonti:

- [Visual Basic main](https://learn.microsoft.com/en-us/dotnet/visual-basic/programming-guide/program-structure/main-procedure)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.vb` | [Hello.vb](Hello.vb) verificato |
| `.vbhtml` | [hello.vbhtml](variants/vbhtml-d3316377/hello.vbhtml) creato, verifiche pendenti |
