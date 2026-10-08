# #534 Pickle

Voce canonica `Pickle`, tipo `data`, language_id `284`.

Leggere un Pickle originale di soli dati che contiene message e language.

## Toolchain e riproduzione

Python standard-library Pickle/Pickletools — 3.13.9. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python standard library pickle e pickletools; file originale protocol 4 generato da pickle.dumps.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python verify.py
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Disassemblaggio genuino seguito da Unpickler nativo che rifiuta qualsiasi riferimento a classi/globali. Il confronto della mappa controlla i dati decodificati.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://docs.python.org/3/library/pickle.html](https://docs.python.org/3/library/pickle.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pkl` | [hello.pkl](hello.pkl) verificato |
