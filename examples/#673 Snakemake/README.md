# #673 Snakemake

Perform a Snakemake rule that prints greeting.

Canonical type `programming`, language_id `151241392`.

Suggested toolchain: Python3.13.9 + Snakemake9.27.0.

From the example directory:

```sh
snakemake --cores 1 hello
```

Expected result: successful workflow and Hello, World! line.

The rule does not create output files; the engine runs the Python run block.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 + Snakemake original engine. [Log](verification/result.json).

Sources:

- [Snakemake rules](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html)

Install the dependencies in a separate directory:

```sh
python -m pip install snakemake
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.smk` | [Snakefile.smk](variants/smk-dec36d46/Snakefile.smk) created; verification pending |
| `.snakefile` | [Snakefile.snakefile](variants/snakefile-94f1120f/Snakefile.snakefile) created; verification pending |
