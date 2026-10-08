# #329 Jac

Eseguire un blocco entry Jac che stampa Hello, World!.

Tipo canonico `programming`, language_id `235277043`.

Toolchain prevista: Python 3.13 e jaclang CLI.

Dalla cartella dell’esempio:

```sh
jac run hello.jac
```

Risultato atteso: stdout Hello, World! e LF, uscita 0.

Il programma non usa walker, servizi, modelli o API esterne: richiede soltanto il runtime Jac.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 + jaclang 0.16.7. [Log](verification/result.json). 

Fonti:

- [Jac — documentazione originale](https://docs.jaseci.org/reference/language/foundation/)
- [Jaseci/Jac — implementazione](https://github.com/Jaseci-Labs/jaseci)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install jaclang==0.16.7
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.jac` | [hello.jac](hello.jac) verificato |
