# #427 Meson

Configure a Meson project and launch a run_target that prints the greeting.

Canonical type `programming`, language_id `799141244`.

Suggested toolchain: Meson, Ninja and Python 3.13.

From the example directory:

```sh
meson setup build
meson compile -C build hello
```

Expected result: target hello successfully executed; stdout contains a Hello, World! line.

The project does not require a C compiler: Meson interprets the recipe and Ninja performs the Python target.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 + Meson 1.12.1 + Ninja 1.13.2. [Log](verification/result.json).

Sources:

- [Meson — run targets](https://mesonbuild.com/Run-targets.html)

Install the dependencies in a separate directory:

```sh
python -m pip install meson==1.12.1 ninja==1.13.2
```
