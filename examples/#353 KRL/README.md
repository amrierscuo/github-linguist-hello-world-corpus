# #353 KRL

Voce canonica `KRL`, tipo `programming`, language_id `186`.

The ruleset reacts to the `corpus:hello` event and sends a `greeting` directive with `message=Hello, World!`.

## Toolchain and reproduction

Picolab Pico Engine core 1.6.4, pico-framework 0.8.1, krl-compiler e krl-parser 1.5.0, Node.js 22.20.0. La baseline Linguist identifica qui Kinetic Rule Language.

From the directory of the example, with dependencies in a dedicated folder external to the sources of the corpus:

```sh
npm install --prefix /path/to/krl-tools pico-engine-core@1.6.4 memory-level@1.0.0 charwise@3.0.1
node verify.cjs /path/to/krl-tools /path/to/krl-build
node verify_runtime.cjs /path/to/krl-tools
```

Replace `/path/to` with your working directories outside the clone. The checker loads the bytes of `hello.krl` with the official loader, compiles them with the original compiler and installs the ruleset in a real pico. The database and loader run in memory. The test starts no HTTP server and downloads no remote ruleset code.

## Status and evidence

Artefatto created, syntax verified, behavior verified su Windows x64.

The test sends first `corpus:unrelated`, which does not generate directives, and then `corpus:hello`. The actual result contains only one `greeting` directive with `options.message` equal to `Hello, World!`. The ruleset is uninstalled and the database closed at the end.

Real log: [runtime.json](verification/runtime.json), with timestamp UTC, versions, commands, exit code, output, hash of sources and checker. The previous test of only parsing remains in [native.json](verification/native.json). Dependences and AST generated remain external to the corpus.

## Primary sources

- [Picolab Pico Engine e componenti ufficiali](https://github.com/Picolab/pico-engine)
- [Picolab pico-framework](https://github.com/Picolab/pico-framework)
- [Grammatica KRL](https://picolabs.atlassian.net/wiki/spaces/docs/pages/223117313/Grammar)

## Extension coverage

Each suffix maintains its own test; the pending variants do not inherit verifications.

| Extension | File and status |
| --- | --- |
| `.krl` | [hello.krl](hello.krl) syntax and behavior verified |
