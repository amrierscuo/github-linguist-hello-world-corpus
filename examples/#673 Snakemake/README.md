# #673 Snakemake

Eseguire una regola Snakemake che stampa il saluto.

Tipo canonico `programming`, language_id `151241392`.

Toolchain prevista: Python3.13.9 + Snakemake9.27.0.

Dalla cartella dell’esempio:

```sh
snakemake --cores 1 hello
```

Risultato atteso: workflow eseguito con successo e riga Hello, World!.

La regola non crea file di output; il motore esegue il run block Python.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 + Snakemake original engine. [Log](verification/result.json). 

Fonti:

- [Snakemake rules](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install snakemake
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.smk` | [Snakefile.smk](variants/smk-dec36d46/Snakefile.smk) creato, verifiche pendenti |
| `.snakefile` | [Snakefile.snakefile](variants/snakefile-94f1120f/Snakefile.snakefile) creato, verifiche pendenti |
