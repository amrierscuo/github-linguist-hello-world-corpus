# #517 PDDL

Solve a PDDL problem whose goal is greeted hello-world.

Canonical type `programming`, language_id `736235603`.

Suggested toolchain: Python and pyperplan.

From the example directory:

```sh
python verify.py
```

Expected result: plan of a hello-world greet action reaches the goal.

PDDL does not print strings: the semantic goal is the valid plan. The adaptor prints the greeting only after comparing the planner.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 + pyperplan 2.1. [Log](verification/result.json).

Sources:

- [pyperplan original planner](https://github.com/aibasel/pyperplan)

Install the dependencies in a separate directory:

```sh
python -m pip install pyperplan
```

Install the dependencies in a separate directory:

```sh
python -m pip install pyperplan==2.1
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pddl` | [hello.pddl](hello.pddl), [problem.pddl](problem.pddl) verified |
