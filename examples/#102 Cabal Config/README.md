# #102 Cabal Config

Descrivere un pacchetto Cabal con un eseguibile Haskell che stampa Hello, World!.

Tipo canonico: `data`; `language_id`: `677095381`.

Toolchain prevista: cabal-install 3.x e GHC con base 4.14–4.x. La versione effettivamente provata, quando disponibile, è nel log.

Dalla cartella dell'esempio, con le dipendenze nel PATH:

```sh
cabal build hello-world
cabal run hello-world
```

Risultato atteso: build accettato e stdout `Hello, World!\n`.

Il .cabal è l’artefatto canonico; Main.hs è il sorgente di supporto. La licenza del corpus deve ancora essere scelta: qui non viene dichiarata una licenza fittizia.

Stato iniziale: artefatto creato, sintassi e semantica in attesa. Toolchain specifica non ancora eseguita su questo esempio; sintassi e semantica restano da verificare.

Fonti primarie o riferimenti originali del progetto:

- [Cabal — formato dei pacchetti](https://cabal.readthedocs.io/en/stable/cabal-package-description-file.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cabal` | [hello-world.cabal](hello-world.cabal) creato, verifiche pendenti |
