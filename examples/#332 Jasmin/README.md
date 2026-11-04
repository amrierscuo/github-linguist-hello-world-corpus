# #332 Jasmin

Assemblare bytecode JVM con Jasmin e chiamare PrintStream.println.

Canonical type `programming`, language_id `180`.

Suggested toolchain: Jasmin 3.0.3 and JDK 21.

From the example directory:

```sh
java -cp "$JASMIN_CLASSPATH" jasmin.Main -d build Hello.j
java -cp build Hello
```

Expected result: bytecode JVM valid; stdout Hello, World! and LF.

The source contains explicit JVM instructions. The assembled class remains out of the corpus.

Recorded status: syntax verified; behavior verified. Toolchain: Jasmin 3.0.3 + CUP 0.9.2 + OpenJDK 21.0.12. [Log](verification/result.json).

Sources:

- [Jasmin — manuale originale](https://jasmin.sourceforge.net/guide.html)
- [Jasmin — progetto Sable](https://github.com/Sable/jasmin)

Classpath required: `jasmin-3.0.3.jar`, `java_cup-0.9.2.jar`. The original JAR are available from [Maven Central](https://repo.maven.apache.org/maven2/). Set the command classpath variable; `;` separator on Windows, `:` on Unix.

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.j` | [Hello.j](Hello.j) verified |
