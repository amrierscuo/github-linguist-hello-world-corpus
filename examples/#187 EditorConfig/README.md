# #187 EditorConfig

Risolvere con EditorConfig le proprietà del file greeting.txt e controllarne testo e terminatore LF.

Tipo canonico `data`, language_id `96139566`.

Toolchain prevista: Python 3 e editorconfig-core-py.

Dalla cartella dell’esempio:

```sh
python verify.py
```

Risultato atteso: proprietà previste UTF-8, LF, newline finale e indentazione di 2 spazi; testo Hello, World! conservato.

Il core risolve la configurazione; non applica modifiche come farebbe un editor. L’obiettivo registrato è la risoluzione delle proprietà e il confronto dei byte del file, non l’integrazione con un IDE.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 + editorconfig-core-py 0.17.1. Vedere [log](verification/verification.log). 

Fonti del linguaggio/formato e implementazioni originali:

- [EditorConfig — specifica e proprietà](https://editorconfig.org/)
- [EditorConfig core Python originale](https://github.com/editorconfig/editorconfig-core-py)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install editorconfig==0.17.1
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.editorconfig` | [.editorconfig](.editorconfig) verificato |
