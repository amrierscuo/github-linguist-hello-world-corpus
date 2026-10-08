# #044 Augeas

Voce canonica: `Augeas`, tipo `programming`, `language_id: 25`.

Mappare Hello, World! seguito da newline nel nodo Augeas greeting, poi verificare il round trip get/put.

## Toolchain e riproduzione

augparse / libaugeas Ubuntu package extracted locally — augparse 1.14.1 <http://augeas.net/>. Ambiente della prova: **Ubuntu 24.04 WSL2/Linux x86_64**.

Richiede Augeas augparse e moduli standard della medesima versione. La prova usa i pacchetti Ubuntu 1.14.1 estratti in work e LD_LIBRARY_PATH locale, senza installazione di sistema.

Comando/procedura dalla directory dell’esempio:

```text
augparse -I . hello.aug
```

Risultato atteso: Exit 0; test get produce { greeting = Hello, World! }; test put ricostruisce Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il sorgente contiene una lens originale e due test nativi. augparse verifica tipi e test; la regex del saluto non sostituisce il parser del linguaggio, è parte della lens stessa.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://augeas.net/docs/lenses.html](https://augeas.net/docs/lenses.html)
- [https://augeas.net/docs/language.html](https://augeas.net/docs/language.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.aug` | [hello.aug](hello.aug) verificato |
