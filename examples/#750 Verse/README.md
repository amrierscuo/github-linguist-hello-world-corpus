# #750 Verse

Eseguire il callback OnBegin di un device Verse e scrivere il saluto nel log UEFN.

Tipo canonico `programming`, language_id `180832205`.

Toolchain prevista: Unreal Editor for Fortnite e Verse compiler.

Dalla cartella dell’esempio:

```sh
Importare il device in un progetto UEFN di prova, Build Verse Code, avviare una sessione.
```

Risultato atteso: device compilato e log contiene Hello, World!.

Richiede la toolchain del gioco; il codice non viene caricato in una sessione pubblica.

Stato iniziale: creato; sintassi e semantica in attesa. UEFN/Verse runtime di prova non disponibile.

Fonti:

- [Epic Verse first program](https://dev.epicgames.com/documentation/en-us/fortnite/create-your-own-device-in-verse)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.verse` | [hello.verse](hello.verse) creato, verifiche pendenti |
