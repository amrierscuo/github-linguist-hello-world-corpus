# #413 MTML

Assegnare una variabile MTML e renderizzare Hello, World!.

Tipo canonico `markup`, language_id `218`.

Toolchain prevista: Movable Type template engine.

Dalla cartella dell’esempio:

```sh
Renderizzare hello.mtml con il motore template Movable Type locale.
```

Risultato atteso: output Hello, World! e newline.

L’assegnazione Var con value non produce output. La lettura senza value produce il nome; non basta interpretare il documento come HTML.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [Movable Type — Var](https://www.movabletype.org/documentation/appendices/tags/var.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mtml` | [hello.mtml](hello.mtml) creato, verifiche pendenti |
