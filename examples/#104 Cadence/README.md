# #104 Cadence

Valutare uno script Cadence 1.0 e ottenere la stringa Hello, World!.

Tipo canonico: `programming`; `language_id`: `270184138`.

Toolchain prevista: Interprete standalone Cadence del progetto onflow/cadence, Go; Cadence 1.x. La versione effettivamente provata, quando disponibile, è nel log.

Dalla cartella dell'esempio, con le dipendenze nel PATH:

```sh
cadence hello.cdc
```

Risultato atteso: il valore restituito da main è la stringa `Hello, World!`.

È uno script puro, senza contratti, conti, chiavi o transazioni sulla rete. La sintassi access(all) appartiene a Cadence 1.x.

Stato iniziale: artefatto creato, sintassi e semantica in attesa. Toolchain specifica non ancora eseguita su questo esempio; sintassi e semantica restano da verificare.

Fonti primarie o riferimenti originali del progetto:

- [Cadence — funzioni](https://cadence-lang.org/docs/language/functions)
- [Cadence — interprete standalone originale](https://github.com/onflow/cadence/tree/master/cmd/main)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cdc` | [hello.cdc](hello.cdc) creato, verifiche pendenti |
