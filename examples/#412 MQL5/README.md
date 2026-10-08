# #412 MQL5

Eseguire uno script MQL5 che scrive il saluto nel registro locale.

Tipo canonico `programming`, language_id `427`.

Toolchain prevista: MetaTrader 5 MetaEditor/compiler.

Dalla cartella dell’esempio:

```sh
Compilare hello.mq5 in MetaEditor; eseguire lo script nel terminale di prova.
```

Risultato atteso: compilazione senza errori; registro Experts contiene Hello, World!.

Esempio distinto da MQL4. Nessuna funzione di trading o comunicazione.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain MetaTrader 5 non disponibile.

Fonti:

- [MetaQuotes — MQL5 OnStart](https://www.mql5.com/en/docs/event_handlers/onstart)
- [MetaQuotes — MQL5 Print](https://www.mql5.com/en/docs/common/print)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mq5` | [hello.mq5](hello.mq5), [driver.mq5](variants/mqh-c969556a/driver.mq5) creato, verifiche pendenti |
| `.mqh` | [hello.mqh](variants/mqh-c969556a/hello.mqh) creato, verifiche pendenti |
