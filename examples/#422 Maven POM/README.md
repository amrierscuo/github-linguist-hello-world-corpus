# #422 Maven POM

Interpret a POM Maven, fill out a Java program and create a JAR with greeting.

Canonical type `data`, language_id `226`.

Suggested toolchain: Apache Maven 3.9.x and JDK 21.

From the example directory:

```sh
mvn package
java -cp target/hello-world-1.0.0.jar corpus.Hello
```

Expected result: Maven package successful; program in JAR printing Hello, World! and LF.

The artifacts and plug-ins come from Maven Central. The corpus.build.directory parameter allows you to isolate the files generated outside the corpus.

Recorded status: syntax verified; behavior verified. Toolchain: Apache Maven 3.9.9 + OpenJDK 21.0.12. [Log](verification/result.json).

Sources:

- [Apache Maven — POM reference](https://maven.apache.org/pom.html)
