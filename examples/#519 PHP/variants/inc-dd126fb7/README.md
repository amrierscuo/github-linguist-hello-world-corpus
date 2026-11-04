# 0519: PHP: `.inc`

Role: Includes PHP with function; driver requires file and print value.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: PHP 8.3.6 native Ubuntu CLI. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
php -l hello.inc; php driver.php
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `driver.php`: `75283047904107e54ee5c21d5d203f3becc6ab4a5b2082eb88d96b1d11d92649`
- `hello.inc`: `7291d1b8718b1b36377f1dfc0023f57b75d9f5a76c7118e594f3c6fee9d65729`

Primary sources:

- https://www.php.net/manual/en/function.include.php
- https://www.php.net/manual/en/function.echo.php
