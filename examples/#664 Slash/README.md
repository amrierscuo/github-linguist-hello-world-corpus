# #664 Slash

Valutare un template Slash e renderizzare il saluto.

Tipo canonico `programming`, language_id `349`.

Toolchain prevista: Slash CLI SAPI originale.

Dalla cartella dell’esempio:

```sh
slash-cli hello.sl
```

Risultato atteso: stdout Hello, World! e newline.

Il template usa l’output expression di Slash; Ruby ERB non verifica il suo motore.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [Slash](https://github.com/slash-lang/slash)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sl` | [hello.sl](hello.sl) creato, verifiche pendenti |
