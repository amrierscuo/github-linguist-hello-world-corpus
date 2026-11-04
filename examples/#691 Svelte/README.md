# #691 Svelte

Voce canonica `Svelte`, tipo `markup`, language_id `928734530`.

Fill and render a Svelte5 component with name parameter.

## Toolchain and reproduction

Official svelte compiler/parser and server renderr, 5.57.2. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Compiler and server maker original Svelte, precise version in the log.

Comando/procedura from the directory of the example, unless explicit indications:

```text
npm install --prefix .tools svelte; node verify.cjs .tools build
```

Expected result: Hello, World! in the conformed result, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Il compilatore emette ESM reale e server.render produce World e Reader corretti. Il goal eÌâ‚¬ SSR; il browser non eÌâ‚¬ necessario.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://svelte.dev/docs/svelte/svelte-server](https://svelte.dev/docs/svelte/svelte-server)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.svelte` | [Greeting.svelte](Greeting.svelte) verified |
