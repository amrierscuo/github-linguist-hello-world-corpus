# #752 Vim Help File

Generate helptags with Vim and solve the hello-world tag in documentation.

Canonical type `prose`, language_id `508563686`.

Suggested toolchain: Vim help engine.

From the example directory:

```sh
Copiare hello.txt in una directory doc di prova; :helptags doc; :help hello-world
```

Expected result: help tag solved; buffer help contains the Hello, World! line.

The tag is read by the Vim help engine; it does not just search for the string with Python.

Recorded status: syntax verified; behavior verified. Toolchain: Vim9 native help tag resolver. [Log](verification/result.json).

Sources:

- [Vim help writing](https://vimhelp.org/helphelp.txt.html#help-writing)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.txt` | [hello.txt](hello.txt) verified |
