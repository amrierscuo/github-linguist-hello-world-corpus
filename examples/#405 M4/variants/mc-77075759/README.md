# 0405: M4: `.mc`

Role: Configuration m4/sendmail: greeting in VERSIONID, not a renamed main m4.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: GNU M4 extracted Ubuntu package. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Dalla distribuzione sendmail-cf: m4 hello.mc > hello.cf (offline; non avviare sendmail)
```

Expected result: Configuration sendmail text with VERSIONID greeting

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.mc`: `ac14cf978206c61aa6836be1be472547b2b93f3e26faa81debd8b5c24f141586`

Primary sources:

- https://www.sendmail.org/~ca/email/doc8.12/cf/m4/README
- https://www.gnu.org/software/m4/manual/m4.html
