# #746 Valve Data Format

Analizzare Valve Data Format e leggere il valore message.

Tipo canonico `data`, language_id `544060961`.

Toolchain prevista: Python3.13.9 + ValvePython vdf3.4.

Dalla cartella dell’esempio:

```sh
python verify.py
```

Risultato atteso: struttura KeyValues con saluto.

Si usa il formato testuale KeyValues, non JSON.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 + ValvePython vdf parser. [Log](verification/result.json). 

Fonti:

- [Valve KeyValues](https://developer.valvesoftware.com/wiki/KeyValues)
- [vdf parser](https://github.com/ValvePython/vdf)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install vdf
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.vdf` | [hello.vdf](hello.vdf) verificato |
| `.vmf` | [hello.vmf](variants/vmf-33d6e045/hello.vmf) creato, verifiche pendenti |
