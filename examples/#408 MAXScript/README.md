# #408 MAXScript

Scrivere il saluto nel MAXScript Listener.

Tipo canonico `programming`, language_id `217`.

Toolchain prevista: Autodesk 3ds Max MAXScript runtime.

Dalla cartella dell’esempio:

```sh
Eseguire fileIn "hello.ms" nel MAXScript Listener di una scena di prova.
```

Risultato atteso: Listener mostra Hello, World! e newline.

Nessuna operazione sulla scena; la verifica richiede il runtime proprietario MAXScript.

Stato iniziale: creato; sintassi e semantica in attesa. Runtime Autodesk 3ds Max non disponibile.

Fonti:

- [Autodesk — MAXScript format](https://help.autodesk.com/view/MAXDEV/2026/ENU/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ms` | [hello.ms](hello.ms) creato, verifiche pendenti |
| `.mcr` | [hello.mcr](variants/mcr-27698a41/hello.mcr) creato, verifiche pendenti |
