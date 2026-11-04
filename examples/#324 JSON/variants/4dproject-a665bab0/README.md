# 0324: JSON: `.4DProject`

Ruolo: Descriptor di progetto 4D con commento riconosciuto; nessuna base dati binaria.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Python 3.13.9 json standard library. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
python -m json.tool hello.4DProject; poi usare il validatore/lettore originale dello schema (il parsing JSON non dimostra lo schema prodotto).
```

Expected result: JSON document recognized in the specific scheme; greeting in the indicated field.

Individual status: artifact created `true`, syntax verified `true`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The language parser accepted the file; the application-specific schema, loader and semantics remain unverified.

SHA-256 of variant files:

- `hello.4DProject`: `6019c386a0188b4ed9fc7420eb82d7484d3c5dfa48a24827371d743ae4b5f653`

Primary sources:

- https://developer.4d.com/docs/18/Project/architecture
- https://github.com/github-linguist/linguist/blob/main/samples/JSON/4DPopGit.4DProject
- https://www.rfc-editor.org/rfc/rfc8259

Additive test actually performed:

Parsing JSON/JSON Lines real of the canonical grammar alone; no progetto/configurazione application scheme has been validated.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: 3.13.9
