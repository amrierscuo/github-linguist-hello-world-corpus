# #403 M

Eseguire una routine M/MUMPS che scrive il saluto.

Tipo canonico `programming`, language_id `214`.

Toolchain prevista: YottaDB o GT.M con routine M abilitata.

Dalla cartella dell’esempio:

```sh
yottadb -run HELLO
```

Risultato atteso: stdout Hello, World! e LF.

In M lo spazio iniziale distingue i comandi dalle etichette. Per il runtime installare la routine come HELLO.m in una directory di routine dedicata; il .mumps resta l’artefatto canonico.

Stato iniziale: creato; sintassi e semantica in attesa. Runtime YottaDB/GT.M non ancora disponibile.

Fonti:

- [YottaDB — programmare in M](https://docs.yottadb.com/ProgrammersGuide/langfeat.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mumps` | [hello.mumps](hello.mumps) creato, verifiche pendenti |
| `.m` | [hello.m](variants/m-f7140aa0/hello.m) creato, verifiche pendenti |
