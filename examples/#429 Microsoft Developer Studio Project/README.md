# #429 Microsoft Developer Studio Project

## Verified on November 19, 2026

A compatible reader resolved the original VC6 project configuration, selected its declared source and applied its preprocessor definitions. The generated C console program printed the exact greeting.

Run `Select CFG and SOURCE from hello.dsp, compile with its mapped debug defines and run the generated console target`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

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
| `.dsp` | [hello.dsp](hello.dsp) Syntax and behavior verified |

</details>
