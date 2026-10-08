# #753 Vim Snippet

Espandere uno snippet UltiSnips per ottenere il saluto.

Tipo canonico `markup`, language_id `81265970`.

Toolchain prevista: Vim con UltiSnips originale.

Dalla cartella dell’esempio:

```sh
Caricare hello.snippets come filetype fixture; digitare hello e attivare l’espansione.
```

Risultato atteso: buffer contiene Hello, World!.

La verifica richiede il loader e l’espansore, non un parser inventato per queste tre righe.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [UltiSnips](https://github.com/SirVer/ultisnips/blob/master/doc/UltiSnips.txt)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.snip` | [hello.snip](variants/snip-4fb5d1ae/hello.snip) creato, verifiche pendenti |
| `.snippet` | [hello.snippet](variants/snippet-29acba5e/hello.snippet) creato, verifiche pendenti |
| `.snippets` | [hello.snippets](hello.snippets) creato, verifiche pendenti |
