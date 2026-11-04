# #672 Smithy

Assemble a Smithy model and read the enum HELLO value from the semantic model.

Canonical type `programming`, language_id `1027892786`.

Suggested toolchain: JDK and Smithy model/utils.

From the example directory:

```sh
java -cp "$SMITHY_CLASSPATH" Verify.java
```

Expected result: valid model and enum Hello, World!.

The goal is the IDL model, not a AWS endpoint or a generated client.

Recorded status: syntax verified; behavior verified. Toolchain: JDK21 + Smithy model/utils 1.50.0. [Log](verification/result.json).

Sources:

- [Smithy IDL](https://smithy.io/2.0/spec/idl.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.smithy` | [hello.smithy](hello.smithy) verified |
