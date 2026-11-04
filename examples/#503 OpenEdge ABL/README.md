# #503 OpenEdge ABL

Show greeting in an informative window ABL.

Canonical type `programming`, language_id `264`.

Suggested toolchain: Progress OpenEdge ABL.

From the example directory:

```sh
pro -p hello.p
```

Expected result: alert box with Hello, World!.

It requires the OpenEdge runtime; it is not interpreted as another Pascal.

Initial state: created; syntax and behavioral verification pending. Runtime Progress OpenEdge unavailable.

Sources:

- [Progress MESSAGE](https://docs.progress.com/bundle/abl-reference/page/MESSAGE-statement.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.p` | [hello.p](hello.p), [driver.p](variants/cls-699ea095/driver.p) created; verification pending |
| `.cls` | [CorpusGreeting.cls](variants/cls-699ea095/CorpusGreeting.cls) created; verification pending |
| `.w` | [hello.w](variants/w-931a997c/hello.w) created; verification pending |
