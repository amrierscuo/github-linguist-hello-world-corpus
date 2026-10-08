# #421 Mathematical Programming System

Leggere un modello MPS e risolvere 13 variabili fissate ai codici ASCII del saluto.

Tipo canonico `programming`, language_id `429002699`.

Toolchain prevista: Python 3.13, highspy/HiGHS solver originale.

Dalla cartella dell’esempio:

```sh
python verify.py
```

Risultato atteso: modello accettato, soluzione ottima e vettore ASCII Hello, World!.

Il file è un problema matematico semplice con bounds FX; il saluto viene decodificato dalla soluzione del solver, non letto da un commento.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 + HiGHS/highspy 1.15.1. [Log](verification/result.json). 

Fonti:

- [HiGHS — modello e solver](https://highs.dev/)
- [MPS — formato IBM CPLEX](https://www.ibm.com/docs/en/icos/22.1.2?topic=standard-records-in-mps-format)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install highspy==1.15.1
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mps` | [hello.mps](hello.mps) verificato |
