# #593 RPGLE

Compilare RPGLE free-format e visualizzare il saluto con DSPLY.

Tipo canonico `programming`, language_id `609977990`.

Toolchain prevista: IBM i ILE RPG compiler.

Dalla cartella dell’esempio:

```sh
CRTBNDRPG PGM(TEST/HELLO) SRCSTMF(hello.rpgle)
CALL PGM(TEST/HELLO)
```

Risultato atteso: messaggio DSPLY Hello, World!.

I nomi di libreria e path devono essere adattati ad un IBM i di prova.

Stato iniziale: creato; sintassi e semantica in attesa. IBM i e ILE RPG compiler non disponibili.

Fonti:

- [IBM RPG free form](https://www.ibm.com/docs/en/i/7.5.0?topic=specifications-fully-free-form-statements)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.rpgle` | [hello.rpgle](hello.rpgle) creato, verifiche pendenti |
| `.sqlrpgle` | [hello.sqlrpgle](variants/sqlrpgle-34018e4d/hello.sqlrpgle) creato, verifiche pendenti |
