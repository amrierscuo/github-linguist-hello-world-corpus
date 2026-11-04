# #585 RBS

Analyze an alias RBS type string literal equal to greeting.

Canonical type `data`, language_id `899227493`.

Suggested toolchain: Ruby and RBS parser.

From the example directory:

```sh
ruby verify.rb
```

Expected result: type alias greeting with literal Hello, World!.

A type alias does not perform Ruby. The verification concerns the statement and the value in its AST.

Recorded status: syntax verified; behavior verified. Toolchain: Ruby 3.2.3 + RBS parser. [Log](verification/result.json).

Sources:

- [RBS syntax](https://github.com/ruby/rbs/blob/master/docs/syntax.md)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.rbs` | [hello.rbs](hello.rbs) verified |
