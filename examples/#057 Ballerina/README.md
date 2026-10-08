# #057 Ballerina

Voce canonica: `Ballerina`, tipo `programming`, `language_id: 720859680`.

Concatenare e stampare Hello, World! con io:println in Ballerina.

## Toolchain e riproduzione

bal — non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede una distribuzione Ballerina Swan Lake con modulo ballerina/io. Versione locale non disponibile e da registrare prima della verifica.

Comando/procedura dalla directory dell’esempio:

```text
bal version; bal run hello.bal
```

Risultato atteso: Compilazione ed esecuzione riuscite; stdout Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Sorgente originale con funzione main pubblica e stringa locale. Non è stato compilato o eseguito poiché bal non è presente.

Requisiti residui:

- bal toolchain not installed or not available in this isolated verification environment.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://ballerina.io/learn/by-example/hello-world/](https://ballerina.io/learn/by-example/hello-world/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bal` | [hello.bal](hello.bal) creato, verifiche pendenti |
