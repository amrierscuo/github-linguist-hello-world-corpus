# #195 EmberScript

Fill out an EmberScript source with the original compiler and run the JavaScript to print Hello, World!.

Canonical type `programming`, language_id `103`.

Suggested toolchain: Node.js 22 and ember-script 0.0.14.

From the example directory:

```sh
node verify.cjs
```

Expected result: stdout `Hello, World!\n`, 0. output

Greetings use a call to the console that does not depend on Ember classes. It remains an EmberScript source; it is compiled by its compiler, not by pure CoffeeScript.

Recorded status: syntax verified; behavior verified. Toolchain: Node.js 22.20.0 + ember-script 0.0.14. See [log](verification/verification.log).

Sources of linguaggio/formato and original implementations:

- [EmberScript — progetto originale](https://github.com/ghempton/ember-script)

Install the dependencies in a separate directory:

```sh
npm install --ignore-scripts --no-audit --no-fund ember-script@0.0.14
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.em` | [hello.em](hello.em) verified |
| `.emberscript` | [hello.emberscript](variants/ext-emberscript-2e656d626572736372697074/hello.emberscript) created; verification pending |
