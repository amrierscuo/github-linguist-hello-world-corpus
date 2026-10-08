# #751 Vespa Schema Definition

Validare uno schema Vespa e conservare un campo message leggibile tramite summary.

Tipo canonico `data`, language_id `587879709`.

Toolchain prevista: Vespa application validator e server di prova.

Dalla cartella dell’esempio:

```sh
Validare hello.sd in un application package e caricare document.json in un’istanza isolata.
```

Risultato atteso: schema accettato; document summary restituisce message Hello, World!.

Il contratto e il documento sono originali. La validazione completa richiede il modello Vespa.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [Vespa schema reference](https://docs.vespa.ai/en/reference/schema-reference.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sd` | [hello.sd](hello.sd) creato, verifiche pendenti |
