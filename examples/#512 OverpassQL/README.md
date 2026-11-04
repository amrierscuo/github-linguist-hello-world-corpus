# #512 OverpassQL

Produce a derived Overpass element with tag equal to greeting.

Canonical type `programming`, language_id `689079655`.

Suggested toolchain: Overpass API query engine.

From the example directory:

```sh
Eseguire il file con un motore Overpass locale o Overpass Turbo.
```

Expected result: JSON with derived element greeting and tag message Hello, World!.

make creates a local element and does not require a geographical query; the engine remains necessary.

Stato iniziale: creato; sintassi e semantica in attesa. Motore Overpass locale non disponibile.

Sources:

- [Overpass QL make](https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#The_statement_make)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.overpassql` | [hello.overpassql](hello.overpassql) created; verification pending |
