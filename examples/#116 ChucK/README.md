# #116 ChucK

Stampare il saluto tramite l’operatore di output diagnostico ChucK.

Tipo canonico: `programming`; `language_id`: `57`.

Toolchain prevista: ChucK 1.5.x (opzione silent per non aprire dispositivi audio). La versione effettivamente provata, quando disponibile, è nel log.

Dalla cartella dell'esempio, con le dipendenze nel PATH:

```sh
chuck --silent hello.ck
```

Risultato atteso: output diagnostico contenente la stringa `Hello, World!`, eventuali virgolette e annotazione del tipo string secondo la versione.

L’operatore <<< >>> scrive il testo di debug e il tipo; non genera audio. --silent evita di richiedere un dispositivo sonoro.

Stato iniziale: artefatto creato, sintassi e semantica in attesa. Toolchain specifica non ancora eseguita su questo esempio; sintassi e semantica restano da verificare.

Fonti primarie o riferimenti originali del progetto:

- [ChucK — panoramica del linguaggio](https://chuck.cs.princeton.edu/doc/language/overview.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ck` | [hello.ck](hello.ck) creato, verifiche pendenti |
