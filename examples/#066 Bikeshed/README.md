# #066 Bikeshed

Minimum independent specification that generates the Greeting section with the Hello, World! paragraph.

## Reproduction

Bikeshed 7.1.3 and Python 3.13.9. Install Bikeshed in an isolated Python environment, as from [manuale ufficiale](https://speced.github.io/bikeshed/).

```sh
bikeshed --die-on=everything spec hello.bs hello.html
```

The document uses the general `Status: DREAM` value without `Group`. The generator must end without errors or warning. In the generated HTML, `#greeting` identifies the title Greeting and the next paragraph contains exactly Hello, World!.

## Try

syntax and behavior verified 2026-10-08T23:35:51.294764+00:00: [log nativo](verification/finish_native.json), commands, versions, SHA-256 and values extracted from the real HTML output. The generated output and dependencies remain out of the corpus.

## Primary sources

- [Bikeshed manual](https://speced.github.io/bikeshed/)
- [Bikeshed repository](https://github.com/speced/bikeshed)

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.bs` | [hello.bs](hello.bs) syntax and behavior verified |
