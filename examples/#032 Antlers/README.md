# #032 Antlers

`hello.antlers.html` uses the variable Antlers `audience`. The expected result is `<p>Hello, World!</p>` followed by newline.

Expected prerequisites: a working Statamic 6.x application with Composer, PHP 8.3 or later, and the extensions listed in the documentation. Actual versions have not been recorded because this environment has not been set up or run.

To check, copy `hello.antlers.html` and `verify.php` in **root di una copia temporanea del sito Statamic**, next to `vendor/` and `bootstrap/`. The bootstrap in `verify.php` refers deliberately to this application structure.

```sh
php verify.php
```

The helper uploads the site, invokes `Statamic\Facades\Antlers::parse` with `audience=World` and compares the entire output with the expected result. syntax and behavior remain waiting: the comparison with the documentation and the presence of the helper do not count as a test of the engine.

Toolchain: **Target Statamic 6.x in applicazione Laravel configurata; PHP >=8.3 e Composer; nessuna versione eseguita**.

Status: **Sintassi e semantica in attesa.**

Residual requirement: Statamic application and PHP/Composer environment with unprepared dependencies; parser Antlers not performed.

Primary sources:

- [Documentazione / sorgente ufficiale 1](https://statamic.dev/frontend/antlers)
- [Documentazione / sorgente ufficiale 2](https://statamic.dev/getting-started/requirements)
- [Documentazione / sorgente ufficiale 3](https://github.com/statamic/cms/discussions/8696)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.antlers.html` | [hello.antlers.html](hello.antlers.html) created; verification pending |
| `.antlers.php` | [hello.antlers.php](variants/ext-antlers-php-2e616e746c6572732e706870/hello.antlers.php) created; verification pending |
| `.antlers.xml` | [hello.antlers.xml](variants/ext-antlers-xml-2e616e746c6572732e786d6c/hello.antlers.xml) created; verification pending |
