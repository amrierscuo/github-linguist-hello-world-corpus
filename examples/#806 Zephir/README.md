# #806 Zephir

## Verified on November 18, 2026

The official Zephir generator compiled the unchanged class, and the compiled PHP extension called the original method and printed the greeting.

Run `php zephir.phar generate; phpize; ./configure; make; php -n -d extension=modules/corpus.so -r 'Corpus\Hello::greet();'`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Fill in a Zephir class and call us greet from the PHP extension.

## Toolchain

Zephir compiler; PHP development toolchain

## Procedure

In the project Zephir corpus fill out Hello.zep; load the extension and invoke Corpus\Hello::greet().

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- Zephir/PHP extension compiler/runtime non predisposti.

## Primary sources

- [https://docs.zephir-lang.com/0.18/tutorial/](https://docs.zephir-lang.com/0.18/tutorial/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.zep` | [Hello.zep](Hello.zep) Syntax and behavior verified |

</details>
