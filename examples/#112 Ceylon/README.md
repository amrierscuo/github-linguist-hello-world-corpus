# #112 Ceylon

Compilare ed eseguire una funzione pubblica Ceylon che stampa Hello, World!.

Tipo canonico: `programming`; `language_id`: `54`.

Toolchain prevista: Ceylon 1.3.x e JDK compatibile con la distribuzione Ceylon. La versione effettivamente provata, quando disponibile, è nel log.

Dalla cartella dell'esempio, con le dipendenze nel PATH:

```sh
ceylon compile source/hello.ceylon
ceylon run --run hello default
```

Risultato atteso: stdout `Hello, World!` seguito da newline.

La funzione è nel modulo default e la cartella source segue la convenzione della distribuzione. Un JDK moderno da solo non fornisce il compilatore Ceylon.

Stato iniziale: artefatto creato, sintassi e semantica in attesa. Toolchain specifica non ancora eseguita su questo esempio; sintassi e semantica restano da verificare.

Fonti primarie o riferimenti originali del progetto:

- [Eclipse Ceylon — tour e riga di comando](https://site.ceylon-lang.dev/documentation/1.2/tour/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ceylon` | [hello.ceylon](source/hello.ceylon) creato, verifiche pendenti |
