# #411 MQL4

Eseguire uno script MQL4 che scrive il saluto nel registro locale.

Tipo canonico `programming`, language_id `426`.

Toolchain prevista: MetaTrader 4 MetaEditor/compiler.

Dalla cartella dell’esempio:

```sh
Compilare hello.mq4 in MetaEditor; eseguire lo script nel terminale di prova.
```

Risultato atteso: compilazione senza errori; registro Experts contiene Hello, World!.

Non apre ordini, non legge account e non usa rete. È uno script locale, non un expert advisor operativo.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain MetaTrader 4 non disponibile.

Fonti:

- [MetaQuotes — MQL4 OnStart](https://docs.mql4.com/basis/function/events#onstart)
- [MetaQuotes — Print](https://docs.mql4.com/common/print)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mq4` | [hello.mq4](hello.mq4), [driver.mq4](variants/mqh-c969556a/driver.mq4) creato, verifiche pendenti |
| `.mqh` | [hello.mqh](variants/mqh-c969556a/hello.mqh) creato, verifiche pendenti |
