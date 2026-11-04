# 0341: Jinja: `.j2`

## Recorded verification

**Syntax and behavior verified** on November 4, 2026. Run each original variant's included verifier with official Jinja; exact greeting, Reader and missing-variable controls. [Evidence](../../verification/native_20261104_341_variants_result.json).

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#341 Jinja/hello.jinja.

Required toolchain: Official Jinja compiler/runtime, jinja2 3.1.6. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.j2; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: Hello, World! and PASS of parametric controls.

Earlier status (before this check): Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.j2`: `193487ca91af7ec5fdfd1d0850dfae6f0bbe25258cc0378905c24e65099f8cfb`
- `verify.py`: `e65c4372f6fcde0a04087628c1c84fc91a740aa4a7beadce3906f994e8727d5d`

Primary sources:

- https://jinja.palletsprojects.com/en/stable/api/
- https://jinja.palletsprojects.com/en/stable/templates/
