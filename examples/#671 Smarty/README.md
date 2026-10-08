# #671 Smarty

Compilare e renderizzare Smarty con un parametro target.

Tipo canonico `programming`, language_id `353`.

Toolchain prevista: PHP e Smarty 4.

Dalla cartella dell’esempio:

```sh
php verify.php
```

Risultato atteso: template renderizzato esatto Hello, World! e newline.

SMARTY_HOME indica l’installazione originale e SMARTY_BUILD una directory di cache esterna al corpus.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: PHP 8.3.6 + Smarty 4.5.4 original engine. [Log](verification/result.json). 

Fonti:

- [Smarty templates](https://www.smarty.net/docs/en/language.syntax.tpl)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.tpl` | [hello.tpl](hello.tpl) verificato |
