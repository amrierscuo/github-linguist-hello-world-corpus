# #429 Microsoft Developer Studio Project

Descrivere un progetto console Microsoft Developer Studio 6 con un sorgente C di saluto.

Tipo canonico `data`, language_id `800983837`.

Toolchain prevista: Microsoft Visual C++ 6 Developer Studio.

Dalla cartella dell’esempio:

```sh
msdev hello.dsp /MAKE "Hello - Win32 Debug"
Debug/Hello.exe
```

Risultato atteso: progetto caricato/compilato; programma console stampa Hello, World! e newline.

È un formato legacy .dsp distinto da .vcxproj; l’ambiente Visual C++ 6 resta da predisporre.

Stato iniziale: creato; sintassi e semantica in attesa. Developer Studio/Visual C++ 6 non disponibile.

Fonti:

- [Microsoft — migrazione progetti Visual C++](https://learn.microsoft.com/en-us/cpp/porting/overview-of-potential-upgrade-issues-visual-cpp)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.dsp` | [hello.dsp](hello.dsp) creato, verifiche pendenti |
