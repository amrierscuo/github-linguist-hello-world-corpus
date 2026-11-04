# #112 Ceylon

Fill out and perform a public function Ceylon printing Hello, World!.

Canonical type: `programming`; `language_id`: `54`.

Suggested toolchain: Ceylon 1.3.x and JDK compatible with the Ceylon distribution.

From the example folder, depending on the PATH:

```sh
ceylon compile source/hello.ceylon
ceylon run --run hello default
```

Expected result: stdout `Hello, World!` followed by newline.

The function is in the default module and the source folder follows the distribution convention. A modern JDK alone does not provide the Ceylon compiler.

Initial state: artifact created, syntax and behavioral verification pending. Specific toolchain not yet performed on this example; syntax and behavior remain to be checked.

Primary sources or original references of the project:

- [Eclipse Ceylon — tour e riga di comando](https://site.ceylon-lang.dev/documentation/1.2/tour/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ceylon` | [hello.ceylon](source/hello.ceylon) created; verification pending |
