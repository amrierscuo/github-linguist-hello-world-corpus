# #506 OpenSCAD

Generare un testo tridimensionale del saluto con OpenSCAD.

Tipo canonico `programming`, language_id `266`.

Toolchain prevista: OpenSCAD CLI con font disponibili.

Dalla cartella dell’esempio:

```sh
openscad -o hello.stl hello.scad
```

Risultato atteso: compilazione geometrica riuscita e testo estruso Hello, World!.

L’obiettivo richiede il motore geometrico, non soltanto riconoscere la stringa nel sorgente.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [OpenSCAD text](https://openscad.org/cheatsheet/)
- [OpenSCAD manual text](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Text)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.scad` | [hello.scad](hello.scad) creato, verifiche pendenti |
