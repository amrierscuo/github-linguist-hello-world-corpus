# #334 Java Properties

Upload a Java Properties file and read greeting with java.util.Properties.

Canonical type `data`, language_id `519377561`.

Suggested toolchain: JDK 21 java.util.Properties.

From the example directory:

```sh
java Verify.java
```

Expected result: stdout Hello, World! and LF; correct property.

The file uses ASCII; no ambiguity with the historical coding of Properties.

Recorded status: syntax verified; behavior verified. Toolchain: OpenJDK 21.0.12 Properties. [Log](verification/result.json).

Sources:

- [Java SE — Properties.load](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html#load(java.io.Reader))

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.properties` | [hello.properties](hello.properties) verified |
