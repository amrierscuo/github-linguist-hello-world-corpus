# #588 REXX

Eseguire REXX e stampare il saluto.

Tipo canonico `programming`, language_id `311`.

Toolchain prevista: Regina REXX.

Dalla cartella dell’esempio:

```sh
regina hello.rexx
```

Risultato atteso: stdout Hello, World! e newline.

say è un’istruzione REXX standard.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Regina REXX 3.9.5 native Ubuntu. [Log](verification/result.json). 

Fonti:

- [Regina](https://regina-rexx.sourceforge.io/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.rexx` | [hello.rexx](hello.rexx) verificato |
| `.pprx` | [hello.pprx](variants/pprx-57f86225/hello.pprx) creato, verifiche pendenti |
| `.rex` | [hello.rex](variants/rex-31adbc05/hello.rex) creato, verifiche pendenti |
