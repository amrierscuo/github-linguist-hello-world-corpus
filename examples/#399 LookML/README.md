# #399 LookML

## Verified on November 19, 2026

The compatible lkml parser loaded the original view. The test selected its declared greeting dimension by substituting the derived table alias for the documented TABLE reference and executing the resulting projected query in SQLite. The negative control confirms missing columns are rejected.

Run `python evaluate_view.py hello.view.lkml`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave756_main.json).

[Earlier evidence](verification/result.json).

<details>
<summary>Earlier instructions and evidence</summary>

Describe a derived LookML table that returns greeting as a string size.

## Toolchain

Community lkml 1.3.7 genuine LookML parser; SQLite 3.51.0; Python 3.13.9

## Commands and procedure

python -m pip install -r requirements.txt; python verify.py; load view in the Looker test project and queries of the greeting dimension

## Expected result

Parser accepts view/derived_table/dimension; SQL returns greeting; Looker must validate and question the size.

## Status

syntax verified; behavioral verification pending.

lkml è un parser community esistente, non un validatore implementato qui. SQLite esegue il SQL estratto dal vero AST e trova il saluto. La sostituzione ${TABLE}, connessione e semantica Looker restano pending.

Actual verification of 2026-10-08T12:49:21.017261+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

Remaining requirements:
- Google Looker project/database connection and native validator/runtime pending.

## Primary sources

- [https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table)
- [https://github.com/joshtemple/lkml](https://github.com/joshtemple/lkml)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.lkml` | [hello.view.lkml](hello.view.lkml) Syntax and behavior verified |
| `.lookml` | [hello.lookml](variants/lookml-1f224142/hello.lookml) created; verification pending |

</details>
