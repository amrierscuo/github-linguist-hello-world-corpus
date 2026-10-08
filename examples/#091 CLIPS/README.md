# #091 CLIPS

Inserire un fatto greeting e far scattare esattamente una regola CLIPS che stampa Hello, World! e ritira il fatto.

## Toolchain

Python 3.13.9; clipspy 1.0.6 / bundled native CLIPS engine

## Comandi e procedura

Da questa cartella, con un ambiente Python dotato di clipspy:

```sh
python -m pip install -r requirements.txt
python verify.py
```

La sorgente hello.clp contiene soltanto costrutti CLIPS. verify.py carica i
costrutti, aggiunge un router stdout, esegue reset e run e confronta il numero
di regole eseguite e il testo ottenuto dal motore.

## Risultato atteso

Il motore carica hello.clp, reset inserisce il fatto, run esegue una regola; router riceve Hello, World! più newline.

## Stato

Sintassi e semantica verificate.

verify.py usa le API del motore CLIPS e un router per catturare il suo stdout; non reimplementa l'interprete. Wrapper clipspy e versione sono registrati nel log.

Verifica effettiva del 2026-10-08T11:33:18.759353+00:00 su Windows x64: [log](verification/result.json).
Il log include hash SHA-256 della sorgente e dei checker, versioni, comandi, codici di uscita, stdout, stderr e limiti della prova.

## Fonti primarie

- [https://www.clipsrules.net/](https://www.clipsrules.net/)
- [https://clipsrules.net/documentation/v641/apg641.pdf](https://clipsrules.net/documentation/v641/apg641.pdf)
- [https://clipspy.readthedocs.io/en/latest/index.html](https://clipspy.readthedocs.io/en/latest/index.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.clp` | [hello.clp](hello.clp) verificato |
