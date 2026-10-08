# #517 PDDL

Risolvere un problema PDDL il cui obiettivo è greeted hello-world.

Tipo canonico `programming`, language_id `736235603`.

Toolchain prevista: Python e pyperplan.

Dalla cartella dell’esempio:

```sh
python verify.py
```

Risultato atteso: piano di un’azione greet hello-world raggiunge il goal.

PDDL non stampa stringhe: l’obiettivo semantico è il piano valido. L’adapter stampa il saluto solo dopo aver confrontato il piano del planner.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 + pyperplan 2.1. [Log](verification/result.json). 

Fonti:

- [pyperplan original planner](https://github.com/aibasel/pyperplan)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install pyperplan
```

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install pyperplan==2.1
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pddl` | [hello.pddl](hello.pddl), [problem.pddl](problem.pddl) verificato |
