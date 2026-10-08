# #667 Slint

Compilare un componente Slint con proprietà message e Text collegato al saluto.

Tipo canonico `markup`, language_id `119900149`.

Toolchain prevista: Slint compiler/interpreter.

Dalla cartella dell’esempio:

```sh
slint-viewer hello.slint
```

Risultato atteso: componente accettato e visualizzazione del saluto.

Per la semantica visiva serve il backend UI. Il corpus non apre finestre durante un controllo di sola sintassi.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [Slint language](https://docs.slint.dev/latest/docs/slint/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.slint` | [hello.slint](hello.slint) creato, verifiche pendenti |
