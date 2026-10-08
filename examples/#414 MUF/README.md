# #414 MUF

Inviare un messaggio Hello, World! all’utente locale in un ambiente MUCK di prova.

Tipo canonico `programming`, language_id `219`.

Toolchain prevista: Fuzzball MUCK con compilatore/interprete MUF.

Dalla cartella dell’esempio:

```sh
Compilare hello.muf come programma nel server MUCK locale di prova e invocarlo.
```

Risultato atteso: programma compilato; l’utente che lo esegue riceve Hello, World!.

Nessun collegamento a server pubblici: la semantica richiede un runtime MUCK locale con il destinatario me.

Stato iniziale: creato; sintassi e semantica in attesa. Runtime locale MUCK/MUF non disponibile.

Fonti:

- [Fuzzball — MUF Reference Manual](https://www.fuzzball.org/docs/mufman.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.muf` | [hello.muf](hello.muf) creato, verifiche pendenti |
| `.m` | [hello.m](variants/m-f7140aa0/hello.m) creato, verifiche pendenti |
