# #032 Antlers

`hello.antlers.html` usa la variabile Antlers `audience`. Il risultato previsto è `<p>Hello, World!</p>` seguito da newline.

Prerequisiti previsti: un'applicazione Statamic 6.x funzionante con Composer, PHP 8.3 o successivo ed estensioni richieste dalla documentazione. Le versioni effettive non sono ancora registrate perché questo ambiente non è stato preparato né eseguito.

Per verificare, copiare `hello.antlers.html` e `verify.php` nella **root di una copia temporanea del sito Statamic**, accanto a `vendor/` e `bootstrap/`. Il bootstrap in `verify.php` si riferisce deliberatamente a questa struttura applicativa.

```sh
php verify.php
```

L'helper carica il sito, invoca `Statamic\Facades\Antlers::parse` con `audience=World` e confronta l'intero output con il risultato previsto. Sintassi e semantica restano in attesa: il confronto con la documentazione e la presenza del helper non contano come una prova del motore.

Toolchain: **Target Statamic 6.x in applicazione Laravel configurata; PHP >=8.3 e Composer; nessuna versione eseguita**.

Stato: **Sintassi e semantica in attesa.**

Requisito residuo: Applicazione Statamic e ambiente PHP/Composer con dipendenze non preparati; parser Antlers non eseguito.

Fonti primarie:

- [Documentazione / sorgente ufficiale 1](https://statamic.dev/frontend/antlers)
- [Documentazione / sorgente ufficiale 2](https://statamic.dev/getting-started/requirements)
- [Documentazione / sorgente ufficiale 3](https://github.com/statamic/cms/discussions/8696)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.antlers.html` | [hello.antlers.html](hello.antlers.html) creato, verifiche pendenti |
| `.antlers.php` | [hello.antlers.php](variants/ext-antlers-php-2e616e746c6572732e706870/hello.antlers.php) creato, verifiche pendenti |
| `.antlers.xml` | [hello.antlers.xml](variants/ext-antlers-xml-2e616e746c6572732e786d6c/hello.antlers.xml) creato, verifiche pendenti |
