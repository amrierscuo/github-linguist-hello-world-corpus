# #110 Carbon

Definire la funzione di ingresso Run della toolchain Carbon corrente per stampare Hello, World!.

Tipo canonico: `programming`; `language_id`: `55627273`.

Toolchain prevista: Carbon sperimentale, sintassi del commit df3cf9294397bed0db1aae31aa7c3584dce6a075. La versione effettivamente provata, quando disponibile, è nel log.

Dalla cartella dell'esempio, con le dipendenze nel PATH:

```sh
carbon compile --phase=check hello.carbon
```

Risultato atteso: controllo dei tipi accettato; con la pipeline di esecuzione della stessa toolchain, stampa `Hello, World!\n`.

La sintassi Carbon è sperimentale e viene fissata al commit indicato. Il comando documentato controlla i tipi: non viene scambiato per una prova di esecuzione; linking ed esecuzione restano da provare.

Stato iniziale: artefatto creato, sintassi e semantica in attesa. Toolchain specifica non ancora eseguita su questo esempio; sintassi e semantica restano da verificare.

Fonti primarie o riferimenti originali del progetto:

- [Carbon — esempio originale fissato a commit](https://github.com/carbon-language/carbon-lang/blob/df3cf9294397bed0db1aae31aa7c3584dce6a075/examples/hello_world.carbon)
- [Carbon — driver](https://github.com/carbon-language/carbon-lang/blob/df3cf9294397bed0db1aae31aa7c3584dce6a075/toolchain/docs/driver.md)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.carbon` | [hello.carbon](hello.carbon) creato, verifiche pendenti |
