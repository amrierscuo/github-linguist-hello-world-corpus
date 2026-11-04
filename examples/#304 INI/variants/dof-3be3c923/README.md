# 0304: INI: `.dof`

Role: Project options Delphi 7, not source Pascal.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Python 3.13.9 stdlib configparser. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Esaminare il file con il lettore originale del prodotto. Per unità systemd: systemd-analyze verify FILE (solo offline; non installare/avviare).
```

Expected result: the configuration is recognized and the specified value or description contains the greeting. This does not establish runtime behavior.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.dof`: `5a657b70a395abc78d93cd6a10971fe74ffbb203431edbc9a9c1445200af2726`

Primary sources:

- https://github.com/github-linguist/linguist/blob/main/samples/INI/TOVR.dof
- https://docs.python.org/3/library/configparser.html
