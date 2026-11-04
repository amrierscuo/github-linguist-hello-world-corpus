# #671 Smarty

Fill and make Smarty with a target parameter.

Canonical type `programming`, language_id `353`.

Suggested toolchain: PHP and Smarty 4.

From the example directory:

```sh
php verify.php
```

Expected result: exact rendering template Hello, World! and newline.

SMARTY_HOME indicates the original installation and SMARTY_BUILD an external cache directory to the corpus.

Recorded status: syntax verified; behavior verified. Toolchain: PHP 8.3.6 + Smarty 4.5.4 original engine. [Log](verification/result.json).

Sources:

- [Smarty templates](https://www.smarty.net/docs/en/language.syntax.tpl)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.tpl` | [hello.tpl](hello.tpl) verified |
