# 0295: HiveQL: `.q`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#295 HiveQL/check.py.

Required toolchain: SQLGlot30.21.0 parser Hive; Apache Hive per query runtime non preparato. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.q; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: Query accepted, a greeting line with Hello, World! value.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.hql`: `a5e3aa59529003186d0f7666d6387cefdae6fda7380a1838406f2bf7b6e47952`
- `hello.q`: `4b5b0f638205786e633d8d9cd1c4a0b2421c547d626e46ffbaf71946db0515b0`

Primary sources:

- https://cwiki.apache.org/confluence/spaces/Hive/pages/27362046/LanguageManual+UDF
- https://github.com/tobymao/sqlglot
