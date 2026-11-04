# 0304: INI: `.frm`

Role: Variant with ruolo/formato distinct from the main source.

Provenience: Only block documentation; no artifact with required extension was manufactured.

Required toolchain: Python 3.13.9 stdlib configparser. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Disponibilità del tool originale necessaria; consultare gli impedimenti.
```

Expected result: To check with the native format after the block resolution.

Individual status: artifact created `false`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The extension includes MySQL view descriptor and legacy binary table file. Without genuine export from a compatible server version, no internal metadata such as timestamp, checksum or SQL -mode are invented.

Primary sources:

- https://dev.mysql.com/doc/refman/5.7/en/innodb-multi-versioning.html
- https://github.com/github-linguist/linguist/blob/main/samples/INI/metrics.frm
- https://docs.python.org/3/library/configparser.html
