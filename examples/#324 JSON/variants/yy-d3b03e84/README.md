# 0324: JSON: `.yy`

Role: JSON data of the canon language, with extension associated with languages.yml. Application diagram not verified.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Python 3.13.9 json standard library. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
python -m json.tool hello.yy
```

Expected result: Item JSON with greeting Hello, World!; no validity promise for the associated application.

Individual status: artifact created `true`, syntax verified `true`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The language parser accepted the file; the application-specific schema, loader and semantics remain unverified.
- The GameMaker resource scheme and its IDE version are not verified.

SHA-256 of variant files:

- `hello.yy`: `ea6a04019de5767c9316a9ae80fd4542ed54fb1a46621d4d70e007299d1000fa`

Primary sources:

- https://www.rfc-editor.org/rfc/rfc8259
- https://manual.gamemaker.io/

Additive test actually performed:

Parsing JSON/JSON Lines real of the canonical grammar alone; no progetto/configurazione application scheme has been validated.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: 3.13.9
