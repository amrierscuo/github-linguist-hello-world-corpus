# #328 JSONiq

Evaluate an expression JSONiq that returns a greeting string.

Canonical type `programming`, language_id `177`.

Toolchain provided: RumbleDB, or Zorba with JSONiq support.

From the example directory:

```sh
rumble --query-path hello.jq
```

Expected result: JSONiq sequence with only one item string Hello, World!.

A literal is a valid query: verification requires the JSONiq engine; loading the file with json.loads does not prove this language.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [JSONiq — specifica](https://www.jsoniq.org/docs/JSONiq/html-single/index.html)
- [RumbleDB — motore originale](https://github.com/RumbleDB/rumble)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.jq` | [hello.jq](hello.jq) created; verification pending |
