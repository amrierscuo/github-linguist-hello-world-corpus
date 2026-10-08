# #328 JSONiq

Valutare un’espressione JSONiq che restituisce una stringa di saluto.

Tipo canonico `programming`, language_id `177`.

Toolchain prevista: RumbleDB, oppure Zorba con supporto JSONiq.

Dalla cartella dell’esempio:

```sh
rumble --query-path hello.jq
```

Risultato atteso: sequenza JSONiq con un solo item stringa Hello, World!.

Un literal è una query valida: la verifica richiede il motore JSONiq; caricare il file con json.loads non prova questo linguaggio.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [JSONiq — specifica](https://www.jsoniq.org/docs/JSONiq/html-single/index.html)
- [RumbleDB — motore originale](https://github.com/RumbleDB/rumble)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.jq` | [hello.jq](hello.jq) creato, verifiche pendenti |
