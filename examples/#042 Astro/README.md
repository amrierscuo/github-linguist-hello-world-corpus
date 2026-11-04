# #042 Astro

Voce canonica e ordine originali di reference/languages.yml.

Calculate greeting in the frontmatter Astro and render a HTML document with h1 Hello, World!.

## Toolchain and reproduction

Astro 5.14.1; Node.js 22.20.0. Test performed on Windows x64.

From the example folder, install isolated dependencies and check:

```text
npm --prefix .tools install --save-exact astro@5.14.1
node verify.mjs .tools src/pages/index.astro
```

## Status and evidence

Artefatto created; syntax verified; behavior verified.

The official Astro builder compiles and renders the original source. The frontmatter calculates the greeting and the HTML product file contains the expected h1 title. The old incompatible container is replaced with the normal static build.

Expected result: Hello, World!; for Astro is the content of a h1 in the HTML document.

Log reale: [verification/native.json](verification/native.json) con comandi, versioni, exit code, stdout/stderr e SHA-256. Nessun accesso a servizi cloud o database remoti.

## Primary sources

- [https://docs.astro.build/en/reference/cli-reference/](https://docs.astro.build/en/reference/cli-reference/)
- [https://docs.astro.build/en/basics/astro-components/](https://docs.astro.build/en/basics/astro-components/)

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.astro` | [index.astro](src/pages/index.astro) syntax and behavior verified |
