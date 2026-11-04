# #024 Aiken

Voce canonica: `Aiken`, tipo `programming`, `language_id: 899409497`.
`lib/hello.ak` espone `greeting() -> ByteArray` e restituisce i byte UTF-8 di
`Hello, World!`. Two Aiken tests compare the result with the thirteen bytes
expected and with a different text. `aiken.toml` describes the project without dependencies.

## Toolchain and reproduction

verified on Windows x64 with the official **Aiken v1.1.23+8949565** track.
Install the official 1.1.23 distribution, then from the directory of this example:

```powershell
aiken --version
aiken check --skip-tests .
aiken check .
```

Expected result: typecheck with 0 code and two tests exceeded —
`greeting_has_exact_bytes`, `greeting_rejects_other_text`, without failures.
The tests are performed by the VM Plutus integrated in Aiken.
in the `ByteArray` type represents byte UTF - 8; it is not a message printed on console.

## Status and evidence

Artefact created; syntax **verified**; behavior **verified** in VM.
Negative control: incomplete brackets in the signature of `greeting` rejected by
compiler with 1. code The test uses an isolated copy of the project with the same
bytes of artifacts; does not add build products to the corpus. No requirement
residual for these tests; no wallet or transactions are required.

Log: [aiken.json](verification/aiken.json), con comandi, report completo dei due
test and SHA-256. The official Windows archive has SHA-256
`8f91dfea06a80ddab139db6bce788c7f1a6cc3850c21b44ae6350afe181239ee`,
compared to the runner with the checksum of the distribution. `path_normalization`
describes normalized paths; sources and results are unchanged.

## Official sources

- [ByteArray e notazioni letterali](https://aiken-lang.org/language-tour/primitive-types).
- [Test Aiken e VM](https://aiken-lang.org/language-tour/tests).
- [Distribuzione v1.1.23 e checksum](https://github.com/aiken-lang/aiken/releases/tag/v1.1.23).

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ak` | [hello.ak](lib/hello.ak) verified |
