# 0465: NetLinx: `.axi`

Role: Includes NetLinx with Greeting function, .axs driver distinct from the main program.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: AMX NetLinx Studio/compiler e controller o runtime compatibile; versione da registrare. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
NetLinx Studio: compilare driver.axs e usare controller/emulatore di test
```

Expected result: Hello, World! in local serial log

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `driver.axs`: `d7f6df75a1927e6c9c3be0ca8b75a6fc288b03fb6b20a8e3f4513a677f445720`
- `hello.axi`: `659530a33cde8889dd81a15934209d09fee090ff23e22ef51174995ae668b5b2`

Primary sources:

- https://www.amx.com/en/site_elements/netlinx-programming-language-reference-guide
- https://www.amx.com/ko/site_elements/amx-language-reference-guide-netlinx-programming-language
