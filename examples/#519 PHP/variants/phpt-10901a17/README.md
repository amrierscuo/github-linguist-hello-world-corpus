# 0519: PHP: `.phpt`

Ruolo: Test PHPT originale con sezioni TEST/FILE/EXPECT, distinto da sorgente PHP rinominato.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: PHP 8.3.6 native Ubuntu CLI. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
php /path/to/php-src/run-tests.php hello.phpt
```

Expected result: PASS: FILE output coincides with EXPECT

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.phpt`: `5e9623fea97eb613fc1a3dd4dd20fbcd035482323e55f65a588cfdd7f642f849`

Primary sources:

- https://qa.php.net/phpt_details.php
- https://www.php.net/manual/en/function.echo.php
