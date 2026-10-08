# #105 Cairo

Compilare ed eseguire un programma Cairo moderno che stampa Hello, World!.

Tipo canonico: `programming`; `language_id`: `620599567`.

Toolchain prevista: Scarb 2.11.4 con cairo_execute 2.11.4 (progetto fissato alla versione della guida). La versione effettivamente provata, quando disponibile, è nel log.

Dalla cartella dell'esempio, con le dipendenze nel PATH:

```sh
scarb build
scarb execute
```

Risultato atteso: tra i messaggi di Scarb, una riga `Hello, World!` e uscita 0.

Cairo moderno e Cairo Zero sono voci separate del riferimento. Questo progetto usa l’attributo executable e Scarb; non è un contratto Starknet.

Stato iniziale: artefatto creato, sintassi e semantica in attesa. Toolchain specifica non ancora eseguita su questo esempio; sintassi e semantica restano da verificare.

Fonti primarie o riferimenti originali del progetto:

- [Cairo Book — Hello, World](https://www.starknet.io/cairo-book/ch01-02-hello-world.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cairo` | [lib.cairo](src/lib.cairo) creato, verifiche pendenti |
