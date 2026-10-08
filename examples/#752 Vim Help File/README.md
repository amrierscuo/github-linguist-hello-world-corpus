# #752 Vim Help File

Generare helptags con Vim e risolvere il tag hello-world nella documentazione.

Tipo canonico `prose`, language_id `508563686`.

Toolchain prevista: Vim help engine.

Dalla cartella dell’esempio:

```sh
Copiare hello.txt in una directory doc di prova; :helptags doc; :help hello-world
```

Risultato atteso: help tag risolto; buffer help contiene la riga Hello, World!.

Il tag è letto dal motore help Vim; non si limita a cercare la stringa con Python.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Vim9 native help tag resolver. [Log](verification/result.json). 

Fonti:

- [Vim help writing](https://vimhelp.org/helphelp.txt.html#help-writing)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.txt` | [hello.txt](hello.txt) verificato |
