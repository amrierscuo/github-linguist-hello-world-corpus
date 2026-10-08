# #331 Janet

Stampare Hello, World! usando Janet.

Tipo canonico `programming`, language_id `1028705371`.

Toolchain prevista: Janet CLI originale.

Dalla cartella dell’esempio:

```sh
janet hello.janet
```

Risultato atteso: stdout Hello, World! e LF, uscita 0.

Programma senza dipendenze esterne.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Janet 1.42.1 official Linux x64 release. [Log](verification/result.json). 

Fonti:

- [Janet — manuale](https://janet-lang.org/docs/)
- [Janet — sorgenti e release](https://github.com/janet-lang/janet)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.janet` | [hello.janet](hello.janet) verificato |
