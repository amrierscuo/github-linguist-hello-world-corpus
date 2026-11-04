# 0529: Pascal: `.dfm`

Role: Resorsa form Delphi in text format with Caption del Greeting, not Pascal.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Genuine Free Pascal compiler, 3.2.2. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Delphi: associare hello.dfm a unità TGreetingForm ereditata da TForm; aprire il form in progetto GUI locale
```

Expected result: Title Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.dfm`: `61fd947682af5eeb4a1ab26bd2e3ce1eb65a853b453715df8d55ca1ead6047f2`

Primary sources:

- https://docwiki.embarcadero.com/RADStudio/en/Form_Files
- https://www.freepascal.org/docs.html
