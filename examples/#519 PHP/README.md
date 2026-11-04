# #519 PHP

Run PHP and print your greeting.

Canonical type `programming`, language_id `272`.

Suggested toolchain: PHP CLI.

From the example directory:

```sh
php hello.php
```

Expected result: stdout Hello, World! and newline.

CLI program without web service.

Recorded status: syntax verified; behavior verified. Toolchain: PHP 8.3.6 native Ubuntu CLI. [Log](verification/result.json).

Sources:

- [PHP echo](https://www.php.net/manual/en/function.echo.php)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.php` | [hello.php](hello.php), [driver.php](variants/inc-dd126fb7/driver.php) created; verification pending |
| `.aw` | [hello.aw](variants/aw-61ce44ad/hello.aw) created; verification pending |
| `.ctp` | [hello.ctp](variants/ctp-44fff2c6/hello.ctp) created; verification pending |
| `.fcgi` | [hello.fcgi](variants/fcgi-209194e4/hello.fcgi) created; verification pending |
| `.inc` | [hello.inc](variants/inc-dd126fb7/hello.inc) created; verification pending |
| `.php3` | [hello.php3](variants/php3-408cb19d/hello.php3) created; verification pending |
| `.php4` | [hello.php4](variants/php4-b6a37d4b/hello.php4) created; verification pending |
| `.php5` | [hello.php5](variants/php5-9b1d71b0/hello.php5) created; verification pending |
| `.phps` | [hello.phps](variants/phps-a0d6c078/hello.phps) created; verification pending |
| `.phpt` | [hello.phpt](variants/phpt-10901a17/hello.phpt) created; verification pending |
