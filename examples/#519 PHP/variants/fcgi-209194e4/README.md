# 0519: PHP: `.fcgi`

Role: Entrypoint PHP CGI/FastCGI with shebang, not invented daemon.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: PHP 8.3.6 native Ubuntu CLI. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
php-cgi -l hello.fcgi; PHP-CGI FastCGI host locale con richiesta loopback di test
```

Expected result: Header text/plain and body Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.fcgi`: `c6a4b920b54e61085a64bd51bd914fd3fd659b3779ae490b667342d3ff2a344f`

Primary sources:

- https://www.php.net/manual/en/install.fpm.php
- https://www.php.net/manual/en/function.echo.php
