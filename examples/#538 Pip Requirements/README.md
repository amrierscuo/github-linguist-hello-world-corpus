# #538 Pip Requirements

Voce canonica `Pip Requirements`, tipo `data`, language_id `684385621`.

Risolvere una requirements list Pip per un pacchetto locale originale che restituisce il saluto.

## Toolchain e riproduzione

Actual pip requirements reader/local package resolver and Python — pip 26.1 from <user-home>\AppData\Roaming\Python\Python313\site-packages\pip (python 3.13). Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Pip 26.1 e Python 3.13.9 con setuptools. La prova copia requirements e progetto in work, installa solo nella cartella temporanea e non usa la rete.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python -m pip install --no-index --no-deps --no-build-isolation --target build/installed -r requirements.txt; PYTHONPATH=build/installed python -m corpus_greeting
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il parser/resolver reale di Pip legge la requirement locale, costruisce/install il package originale e il modulo installato stampa il saluto.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://pip.pypa.io/en/stable/reference/requirements-file-format/](https://pip.pypa.io/en/stable/reference/requirements-file-format/)
