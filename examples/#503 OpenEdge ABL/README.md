# #503 OpenEdge ABL

Mostrare il saluto in una finestra informativa ABL.

Tipo canonico `programming`, language_id `264`.

Toolchain prevista: Progress OpenEdge ABL.

Dalla cartella dell’esempio:

```sh
pro -p hello.p
```

Risultato atteso: alert box con Hello, World!.

Richiede il runtime OpenEdge; non viene interpretato come un altro Pascal.

Stato iniziale: creato; sintassi e semantica in attesa. Runtime Progress OpenEdge non disponibile.

Fonti:

- [Progress MESSAGE](https://docs.progress.com/bundle/abl-reference/page/MESSAGE-statement.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.p` | [hello.p](hello.p), [driver.p](variants/cls-699ea095/driver.p) creato, verifiche pendenti |
| `.cls` | [CorpusGreeting.cls](variants/cls-699ea095/CorpusGreeting.cls) creato, verifiche pendenti |
| `.w` | [hello.w](variants/w-931a997c/hello.w) creato, verifiche pendenti |
