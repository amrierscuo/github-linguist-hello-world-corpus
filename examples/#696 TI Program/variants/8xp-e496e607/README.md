# 0696: `.8xp`

TI program - 84 Plus tokenized and contenitore/checksum products really from the original library tivars; source Disp original and generator included. No calcolatrice/emulatore execution declared.

Origin: produttore/serializzatore original executed, as recorded in the log.

Artefatto principale: `hello.8xp`.

Control provided:

```text
python --version
python generate.py
```

Expected result: tivars reinterprets identical "Hello, World!"; execution on TI - 84 Plus still hanging.

State: created; syntax verified; behavior not verified.

Toolchain osservata: tivars 1.1.1; Python 3.13.9.

Ambito reale: Serializzazione/tokenizzazione nativa e roundtrip con tivars. Il parser riconosce il programma e preserva i token di Disp; un runtime TI non è stato eseguito.

Log: `verification/result.json`; SHA-256 of each sorgente/supporto of the variant, commands, exit code and actual output. Build/cache remain under `work/verify_extensions_561_836`.

Blocks: Execution of the program on calcolatrice/emulatore TI - 84 Plus still hanging.

Primary sources:

- [https://github.com/TI-Toolkit/tivars_lib_py](https://github.com/TI-Toolkit/tivars_lib_py)
