# 0387: Linker Script: `.lds`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#387 Linker Script/hello.ld.

Required toolchain: GNU ld (GNU Binutils for Ubuntu) 2.42; GCC 13.3.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.lds; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: Section .greeting contains the text; boundary symbols enclose 14 byte; runtime print greeting.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.lds`: `875d299c757ca4e4a919954f4dc92b066675884ee38f9b7d74ddcc7dd47d8328`
- `main.c`: `31d41a950b832df6e7397dc331bb032117b0eaa03571bc833af6cf63267c8e8b`

Primary sources:

- https://sourceware.org/binutils/docs/ld/SECTIONS.html
- https://sourceware.org/binutils/docs/ld/Miscellaneous-Commands.html
