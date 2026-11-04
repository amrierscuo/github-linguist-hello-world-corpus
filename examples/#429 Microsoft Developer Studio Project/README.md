# #429 Microsoft Developer Studio Project

Describe a Microsoft Developer Studio 6 console project with a greeting source C.

Canonical type `data`, language_id `800983837`.

Suggested toolchain: Microsoft Visual C++ 6 Developer Studio.

From the example directory:

```sh
msdev hello.dsp /MAKE "Hello - Win32 Debug"
Debug/Hello.exe
```

Expected result: caricato/compilato project; Hello, World! and newline press console program.

It is a legacy .dsp format distinct from .vcxproj; the Visual C++ 6 environment remains to be prepared.

Stato iniziale: creato; sintassi e semantica in attesa. Developer Studio/Visual C++ 6 non disponibile.

Sources:

- [Microsoft — migrazione progetti Visual C++](https://learn.microsoft.com/en-us/cpp/porting/overview-of-potential-upgrade-issues-visual-cpp)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.dsp` | [hello.dsp](hello.dsp) created; verification pending |
