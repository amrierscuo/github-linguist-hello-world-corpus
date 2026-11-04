# #047 Avro IDL

Voce canonica: `Avro IDL`, tipo `data`, `language_id: 785497837`.

Fill in a record Avro IDL with default Hello, World!, read the default and save the greeting during encode/decode binary Avro.

## Toolchain and reproduction

Official Apache Avro tools and core Java APIs, 1.12.0. Test environment: **Windows x64**.

Download avro-tools-1.12.0.jar from the official Maven Central repository into .tools. Use a JDK to run the Java source. The local check used Microsoft OpenJDK 21.0.12.1.

Comando/procedura from the example directory:

```text
java -jar .tools/avro-tools-1.12.0.jar idl hello.avdl hello.avpr; java --class-path .tools/avro-tools-1.12.0.jar AvroCheck.java hello.avpr
```

Exit 0; Hello, World!; PASS: compiled IDL default; genuine Avro binary encode/decode.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

AvroCheck.java delegates parsing of the protocol, access to the default and serialization to org.apache.avro; does not implement a Avro parser. The generated protocol and binary data are verified in work.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain and SHA-256 of artifacts. `path_normalization` describes the replacements of artifacts.
machine paths; source bytes remain those identified by checksums.
If the log only records the availability of the tools, no parsing or runtime is attested.
Tools, dependencies and verification products remain in the work directory.

## Primary sources

- [https://avro.apache.org/docs/1.12.0/idl-language/](https://avro.apache.org/docs/1.12.0/idl-language/)
- [https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/generic/GenericData.html](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/generic/GenericData.html)
- [https://repo.maven.apache.org/maven2/org/apache/avro/avro-tools/1.12.0/](https://repo.maven.apache.org/maven2/org/apache/avro/avro-tools/1.12.0/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.avdl` | [hello.avdl](hello.avdl) verified |
