# #106 Cairo Zero

Scrivere nell’output Cairo Zero un felt che codifica in ASCII big-endian Hello, World!.

Tipo canonico: `programming`; `language_id`: `891399890`.

Toolchain prevista: cairo-lang 0.14.x (Cairo Zero) in un ambiente Python compatibile. La versione effettivamente provata, quando disponibile, è nel log.

Dalla cartella dell'esempio, con le dipendenze nel PATH:

```sh
mkdir -p build
cairo-compile hello.cairo --output=build/hello.json
cairo-run --program=build/hello.json --layout=plain --print_output
```

Risultato atteso: output numerico `5735816763073854918203775149089`, che decodificato come byte big-endian dà `Hello, World!`.

Il runtime Zero espone celle di campo, non una console testuale. La stringa corta di 13 byte rientra in un felt. Questo obiettivo riguarda output e decodifica, senza generazione di una prova crittografica.

Stato iniziale: artefatto creato, sintassi e semantica in attesa. Toolchain specifica non ancora eseguita su questo esempio; sintassi e semantica restano da verificare.

Fonti primarie o riferimenti originali del progetto:

- [Cairo Zero — serialize_word originale](https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/serialize.cairo)
- [Cairo Zero — segmenti e output](https://docs.cairo-lang.org/cairozero/how_cairo_works/segments.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cairo` | [hello.cairo](hello.cairo) creato, verifiche pendenti |
