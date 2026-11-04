# #025 Aleo

Voce canonica: `Aleo`, tipo `programming`, `language_id: 566431048`.
`hello.aleo` is written in Aleo Instructions. The `greeting` function, without
arguments, builds a public array of thirteen `u8` that encodes
`Hello, World!` in ASCII. It is a local function of the program
`corpus_hello_world.aleo`; it is not a deployment.

## Toolchain and reproduction

Parser verified su Windows x64 con Node.js **22.20.0** e pacchetto ufficiale
**@provablehq/wasm 0.12.0, mainnet**; SDK 0.12.0 available in the environment.
The Verifier directly imports WASM SnarkVM bindings. From the directory
of this example:

```powershell
npm --prefix .tools install --no-audit --no-fund --save-exact @provablehq/wasm@0.12.0
node verify.cjs .tools/node_modules hello.aleo --syntax-only
```

Syntactic test result: `Program.fromString` accepts the program,
exposes only `greeting` without input and refuses non-existent education.
Both assertions produce `PASS` and the process ends with 0. code
For the behavior test still to be completed:

```powershell
node verify.cjs .tools/node_modules hello.aleo
```

This last command uses an ephemeral key that is not printed and runs the function
offline with `prove_execution=false`; may require initialization of parameters
SnarkVM. The expected output is
`[72u8, 101u8, 108u8, 108u8, 111u8, 44u8, 32u8, 87u8, 111u8, 114u8, 108u8, 100u8, 33u8]`.

## Status and evidence

Artefatto created; syntax **verified**; behavior **in attesa**.
Residual Requirement: Get VM offline execution complete with parameters
the previous attempt via SDK did not have
provided a complete log of execution and is not counted. Current test
is limited to parsing and signing of the function; the temporary XHR of that attempt
they were moved out of the corpus.

Log: [aleo-wasm.json](verification/aleo-wasm.json), with output of the parser,
version, SHA-256 of the source and the verification. `path_normalization` describes
normalized routes; no VM execution result is attested.

## Official sources

- [Tipi e costruzione di array Aleo](https://docs.aleo.org/build/aleo-instructions/reference/types/index.html).
- [SDK e binding SnarkVM WASM ufficiali](https://github.com/ProvableHQ/sdk).

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.aleo` | [hello.aleo](hello.aleo) syntax verified |
