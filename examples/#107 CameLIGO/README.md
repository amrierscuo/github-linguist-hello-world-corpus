# #107 CameLIGO

Interpretare il valore greeting di un modulo CameLIGO e ottenere Hello, World!.

Tipo canonico: `programming`; `language_id`: `829207807`.

Toolchain prevista: LIGO 1.14.2 o una versione con CameLIGO e run interpret. La versione effettivamente provata, quando disponibile, è nel log.

Dalla cartella dell'esempio, con le dipendenze nel PATH:

```sh
ligo run interpret greeting --init-file hello.mligo
```

Risultato atteso: valore stringa `"Hello, World!"`.

L’esempio interpreta un valore del modulo; non invia operazioni Tezos e non richiede un portafoglio.

Stato iniziale: artefatto creato, sintassi e semantica in attesa. Toolchain specifica non ancora eseguita su questo esempio; sintassi e semantica restano da verificare.

Fonti primarie o riferimenti originali del progetto:

- [LIGO — differenze CameLIGO/OCaml](https://ligolang.org/docs/faq/cameligo-ocaml-syntax-diff/)
- [LIGO — run interpret](https://ligolang.org/docs/1.14.2/manpages/run%20interpret/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mligo` | [hello.mligo](hello.mligo) creato, verifiche pendenti |
