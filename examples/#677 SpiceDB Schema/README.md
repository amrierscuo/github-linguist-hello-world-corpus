# #677 SpiceDB Schema

Validare uno schema SpiceDB e una caveat che concede lettura quando message è il saluto.

Tipo canonico `data`, language_id `864005057`.

Toolchain prevista: SpiceDB e zed in ambiente isolato.

Dalla cartella dell’esempio:

```sh
zed validate hello.zed; valutare la caveat greeting in un backend SpiceDB isolato con message="Hello, World!".
```

Risultato atteso: schema accettato; caveat greeting true soltanto per Hello, World!.

L’esempio non modifica un database di autorizzazioni. Il comando esatto dipende dalla versione zed predisposta.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [SpiceDB schema](https://authzed.com/docs/spicedb/concepts/schema)
- [SpiceDB caveats](https://authzed.com/docs/spicedb/concepts/caveats)

zed validate accetta anche file raw .zed; il controllo della caveat in un backend rimane un requisito distinto. [CLI originale](https://github.com/authzed/zed/blob/main/internal/cmd/validate.go).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.zed` | [hello.zed](hello.zed) creato, verifiche pendenti |
