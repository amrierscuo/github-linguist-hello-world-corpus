# #510 Org

Analizzare un documento Org e recuperare il titolo del primo nodo.

Tipo canonico `prose`, language_id `267`.

Toolchain prevista: Python e orgparse.

Dalla cartella dell’esempio:

```sh
python verify.py
```

Risultato atteso: un heading con testo Hello, World!.

La verifica certifica il parsing della struttura Org, senza dichiarare un export Emacs.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 + orgparse 0.5.20260926. [Log](verification/result.json). 

Fonti:

- [Org syntax](https://orgmode.org/worg/dev/org-syntax.html)
- [orgparse](https://github.com/karlicoss/orgparse)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install orgparse
```

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install orgparse==0.5.20260926
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.org` | [hello.org](hello.org) verificato |
