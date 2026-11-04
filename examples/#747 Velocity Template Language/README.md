# #747 Velocity Template Language

Renderizzare Velocity Template Language con parametro target.

Canonical type `markup`, language_id `292377326`.

Suggested toolchain: JDK and Apache Velocity engine.

From the example directory:

```sh
java -cp "$VELOCITY_CLASSPATH" Verify.java
```

Expected result: exact output Hello, World! and newline.

The Apache engine interprets the $target reference.

Recorded status: syntax verified; behavior verified. Toolchain: JDK21 + Apache Velocity2.4.1/CommonsLang3.17/SLF4J2.0.16. [Log](verification/result.json).

Sources:

- [Apache Velocity VTL](https://velocity.apache.org/engine/2.4.1/user-guide.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.vtl` | [hello.vtl](hello.vtl) verified |
