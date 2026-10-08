# #679 Squirrel

Eseguire Squirrel e stampare il saluto.

Tipo canonico `programming`, language_id `355`.

Toolchain prevista: Squirrel sq CLI originale.

Dalla cartella dell’esempio:

```sh
sq hello.nut
```

Risultato atteso: stdout Hello, World! e newline.

Il runtime sq deve essere Squirrel, non un altro tool con lo stesso nome.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Squirrel 3.2 original sources + native GNU C++ build. [Log](verification/result.json). 

Fonti:

- [Squirrel](http://www.squirrel-lang.org/squirreldoc/reference/language.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.nut` | [hello.nut](hello.nut) verificato |
