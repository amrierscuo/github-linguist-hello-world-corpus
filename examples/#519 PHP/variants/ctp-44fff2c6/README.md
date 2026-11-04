# 0519: PHP: `.ctp`

Role: Template CakePHP historical .ctp with HTML output of greeting.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: PHP 8.3.6 native Ubuntu CLI. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
CakePHP 3: renderizzare hello.ctp con helper globale h disponibile
```

Expected result: <p> Hello, World! </p>

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.ctp`: `7a44a503c8c2624438747d21638c303f9d76de794e05e97acacd79f0ac3d2d5c`

Primary sources:

- https://book.cakephp.org/3/en/views.html
- https://www.php.net/manual/en/function.echo.php
