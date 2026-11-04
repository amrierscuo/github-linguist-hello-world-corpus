# #099 CSV

Read CSV the field quoted Hello, World! without dividing it on the inner comma, then rewrite the same data with CRLF.

## Toolchain

Python 3.13.9; stdlib csv

## Commands and procedure

From this folder, without external dependencies:

```sh
python --version
python verify.py
```

The greeting is between double apex because it contains a comma. verify.py law with
newline='' e csv.reader(strict=True), controlla tutte le celle e riscrive con
csv.writer and CRLF; it compares bytes with the original.

## Expected result

Two rows and one column: greeting header, Hello, World! value; roundtrip byte per byte equal to the original UTF-8/CRLF. file

## Status

syntax and behavior verified.

Parser csv standard in strict mode, comma delimiter and quotachar double apex. Control includes comma in the field and CRLF terminators.

Actual verification of 2026-10-08T11:33:46.142758+00:00 on Windows x64: [log](verification/result.json).
The log includes hash SHA-256 of the source and the checkers, versions, commands, exit codes, stdout, stderr and test limits.

## Primary sources

- [https://docs.python.org/3.13/library/csv.html](https://docs.python.org/3.13/library/csv.html)
- [https://www.rfc-editor.org/rfc/rfc4180](https://www.rfc-editor.org/rfc/rfc4180)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.csv` | [hello.csv](hello.csv) verified |
