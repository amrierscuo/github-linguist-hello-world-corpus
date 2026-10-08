# #665 Slice

Compilare una definizione Slice Ice con costante string message.

Tipo canonico `programming`, language_id `894641667`.

Toolchain prevista: ZeroC Ice slice2cpp e SDK Ice.

Dalla cartella dell’esempio:

```sh
slice2cpp --output-dir build hello.ice
```

Risultato atteso: definizione accettata e costante Greeting::message uguale al saluto.

Il file definisce una costante, senza server, proxy o comunicazioni di rete.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [Ice Slice](https://docs.zeroc.com/ice/latest/the-slice-language)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ice` | [hello.ice](hello.ice) creato, verifiche pendenti |
