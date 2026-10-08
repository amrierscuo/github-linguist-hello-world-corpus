# #348 Jupyter Notebook

Voce canonica `Jupyter Notebook`, tipo `markup`, language_id `185`.

Validare un notebook originale e avviarne il kernel Python reale per calcolare e stampare il saluto.

## Toolchain e riproduzione

Official nbformat, nbclient and genuine Jupyter Python kernel — nbformat 5.10.4; nbclient 0.10.2; ipykernel 7.1.0. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

nbformat 5.10.4, nbclient 0.10.2 e ipykernel 7.1.0 già presenti. Richiede il kernelspec python3 locale. Il notebook iniziale ha output vuoti; la copia eseguita resta in build.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python verify.py hello.ipynb build
```

Risultato atteso: Notebook valido; cella eseguita una volta; stdout Hello, World!; PASS.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il validator autentico controlla la struttura prima e dopo l’esecuzione. Il kernel esegue la cella originale e il controllo confronta execution_count e stream stdout; il log registra l’hash del notebook prodotto. Un warning Windows ZMQ sulla selector thread non impedisce l’esecuzione.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://nbformat.readthedocs.io/en/latest/](https://nbformat.readthedocs.io/en/latest/)
- [https://nbclient.readthedocs.io/en/latest/client.html](https://nbclient.readthedocs.io/en/latest/client.html)
- [https://jupyter.org/](https://jupyter.org/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ipynb` | [hello.ipynb](hello.ipynb) verificato |
