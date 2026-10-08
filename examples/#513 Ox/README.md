# #513 Ox

Eseguire main Ox e stampare il saluto.

Tipo canonico `programming`, language_id `268`.

Toolchain prevista: Ox Console/OxMetrics e oxstd.

Dalla cartella dell’esempio:

```sh
oxl hello.ox
```

Risultato atteso: stdout Hello, World! seguito da newline.

Ox è il linguaggio econometrico di Jurgen Doornik; non viene sostituito con un compiler C.

Stato iniziale: creato; sintassi e semantica in attesa. Runtime Ox non disponibile.

Fonti:

- [Ox documentation](https://www.doornik.com/ox/ox.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ox` | [hello.ox](hello.ox), [hello.ox](variants/oxh-134bfc42/hello.ox) creato, verifiche pendenti |
| `.oxh` | [hello.oxh](variants/oxh-134bfc42/hello.oxh) creato, verifiche pendenti |
| `.oxo` | artefatto da generare Oggetto Ox compilato: richiede compilazione originale della versione target; nessun file binario o sorgente .ox rinominato viene prodotto. |
