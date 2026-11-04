# #329 Jac

Perform an entry block Jac printing Hello, World!.

Canonical type `programming`, language_id `235277043`.

Suggested toolchain: Python 3.13 and jaclang CLI.

From the example directory:

```sh
jac run hello.jac
```

Expected result: stdout Hello, World! and LF, 0. output

The program does not use walkers, services, models or external API: it requires only the Jac runtime.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 + jaclang 0.16.7. [Log](verification/result.json).

Sources:

- [Jac — documentazione originale](https://docs.jaseci.org/reference/language/foundation/)
- [Jaseci/Jac — implementazione](https://github.com/Jaseci-Labs/jaseci)

Install the dependencies in a separate directory:

```sh
python -m pip install jaclang==0.16.7
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.jac` | [hello.jac](hello.jac) verified |
