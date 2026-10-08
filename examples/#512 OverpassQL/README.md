# #512 OverpassQL

Produrre un elemento derivato Overpass con tag message uguale al saluto.

Tipo canonico `programming`, language_id `689079655`.

Toolchain prevista: Overpass API query engine.

Dalla cartella dell’esempio:

```sh
Eseguire il file con un motore Overpass locale o Overpass Turbo.
```

Risultato atteso: JSON con derived element greeting e tag message Hello, World!.

make crea un elemento locale e non richiede una query geografica; il motore resta necessario.

Stato iniziale: creato; sintassi e semantica in attesa. Motore Overpass locale non disponibile.

Fonti:

- [Overpass QL make](https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#The_statement_make)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.overpassql` | [hello.overpassql](hello.overpassql) creato, verifiche pendenti |
