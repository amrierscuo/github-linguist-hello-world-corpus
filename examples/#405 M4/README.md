# #405 M4

Espandere una macro GNU M4 per comporre Hello, World!.

Tipo canonico `programming`, language_id `215`.

Toolchain prevista: GNU M4.

Dalla cartella dell’esempio:

```sh
m4 hello.m4
```

Risultato atteso: stdout Hello, World! e LF.

La macro target viene espansa dal processore M4 reale.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: GNU M4 extracted Ubuntu package. [Log](verification/result.json). 

Fonti:

- [GNU M4 — manuale](https://www.gnu.org/software/m4/manual/m4.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.m4` | [hello.m4](hello.m4) verificato |
| `.mc` | [hello.mc](variants/mc-77075759/hello.mc) creato, verifiche pendenti |
