# #519 PHP

Eseguire PHP e stampare il saluto.

Tipo canonico `programming`, language_id `272`.

Toolchain prevista: PHP CLI.

Dalla cartella dell’esempio:

```sh
php hello.php
```

Risultato atteso: stdout Hello, World! e newline.

Programma CLI senza servizio web.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: PHP 8.3.6 native Ubuntu CLI. [Log](verification/result.json). 

Fonti:

- [PHP echo](https://www.php.net/manual/en/function.echo.php)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.php` | [hello.php](hello.php), [driver.php](variants/inc-dd126fb7/driver.php) creato, verifiche pendenti |
| `.aw` | [hello.aw](variants/aw-61ce44ad/hello.aw) creato, verifiche pendenti |
| `.ctp` | [hello.ctp](variants/ctp-44fff2c6/hello.ctp) creato, verifiche pendenti |
| `.fcgi` | [hello.fcgi](variants/fcgi-209194e4/hello.fcgi) creato, verifiche pendenti |
| `.inc` | [hello.inc](variants/inc-dd126fb7/hello.inc) creato, verifiche pendenti |
| `.php3` | [hello.php3](variants/php3-408cb19d/hello.php3) creato, verifiche pendenti |
| `.php4` | [hello.php4](variants/php4-b6a37d4b/hello.php4) creato, verifiche pendenti |
| `.php5` | [hello.php5](variants/php5-9b1d71b0/hello.php5) creato, verifiche pendenti |
| `.phps` | [hello.phps](variants/phps-a0d6c078/hello.phps) creato, verifiche pendenti |
| `.phpt` | [hello.phpt](variants/phpt-10901a17/hello.phpt) creato, verifiche pendenti |
