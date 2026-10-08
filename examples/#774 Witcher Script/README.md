# #774 Witcher Script

Voce canonica `Witcher Script`, tipo `programming`, language_id `686821385`.

Funzione globale WitcherScript originale CorpusGreeting() che restituisce `Hello, World!` come string.

## Toolchain e riproduzione

CD Projekt RED WitcherScript compiler / REDkit — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Occorre il compilatore WitcherScript del gioco o REDkit, con versione compatibile. La guida del produttore descrive funzioni globali, tipi e ambiente di compilazione.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
In REDkit / The Witcher 3: aggiungere hello.ws a una mod di prova sotto content/scripts; compilare gli script; invocare CorpusGreeting() da un harness di debug e confrontare il risultato.
```

Risultato atteso: Compilazione riuscita e CorpusGreeting() uguale a Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Ambiente proprietario assente: la funzione è creata, ma nessun parser generico o sola lettura è usato per segnare verifiche positive.

Requisiti residui:

- Compilatore/runtime WitcherScript e REDkit assenti.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://cdprojektred.atlassian.net/wiki/spaces/W3REDkit/pages/36306960/WitcherScript](https://cdprojektred.atlassian.net/wiki/spaces/W3REDkit/pages/36306960/WitcherScript)
- [https://cdprojektred.atlassian.net/wiki/spaces/W3REDkit/pages/36307090/WS+Language+Guide](https://cdprojektred.atlassian.net/wiki/spaces/W3REDkit/pages/36307090/WS+Language+Guide)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ws` | [hello.ws](hello.ws) creato, verifiche pendenti |
