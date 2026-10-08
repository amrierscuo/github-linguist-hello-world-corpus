# #676 SourcePawn

Compilare un plugin SourcePawn che stampa il saluto al suo caricamento.

Tipo canonico `programming`, language_id `354`.

Toolchain prevista: SourceMod spcomp e un server Source engine di prova.

Dalla cartella dell’esempio:

```sh
spcomp hello.sp -o build/hello.smx
```

Risultato atteso: plugin compilato e console server contiene Hello, World!.

Il compiler prova il plugin; il callback richiede il server di gioco per la semantica.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [SourcePawn](https://wiki.alliedmods.net/Introduction_to_SourcePawn_1.7)
- [SourceMod](https://www.sourcemod.net/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sp` | [hello.sp](hello.sp), [main.sp](variants/inc-dd126fb7/main.sp) creato, verifiche pendenti |
| `.inc` | [hello.inc](variants/inc-dd126fb7/hello.inc) creato, verifiche pendenti |
