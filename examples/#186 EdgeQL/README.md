# #186 EdgeQL

Valutare una query EdgeQL che restituisce un singleton di tipo str contenente Hello, World!.

Tipo canonico `programming`, language_id `925235833`.

Toolchain prevista: Gel/EdgeDB server e client CLI compatibili.

Dalla cartella dell’esempio:

```sh
gel query --file hello.edgeql
```

Risultato atteso: insieme singleton {'Hello, World!'}.

La query è di sola lettura e non richiede uno schema applicativo. Un server Gel locale è comunque necessario per la verifica effettiva.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain nativa non ancora eseguita: le verifiche di sintassi e semantica restano pendenti.

Fonti del linguaggio/formato e implementazioni originali:

- [EdgeQL — SELECT](https://docs.geldata.com/reference/edgeql/select)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.edgeql` | [hello.edgeql](hello.edgeql) creato, verifiche pendenti |
| `.esdl` | [hello.esdl](variants/ext-esdl-2e6573646c/hello.esdl) creato, verifiche pendenti |
