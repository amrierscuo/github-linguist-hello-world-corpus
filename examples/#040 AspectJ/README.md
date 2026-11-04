# #040 AspectJ

Print Hello, World! from an AspectJ before advice, applied to the execution of the Java HelloWorld.greet method through weaving in compilation.

## File

- `Greeting.aj`
- `HelloWorld.java`

## Toolchain and verification

AspectJ ajc/aspectjrt 1.9.22; Microsoft OpenJDK 21.0.12.1; Sources and bytecode Java 17.x

Download `aspectjtools-1.9.22.jar` and `aspectjrt-1.9.22.jar` from directories
Maven officers listed below; place them in a tool folder outside the
corpus. The following commands use relative paths for simplicity: adapt them
to the actual location of JAR. Run from the example folder with
JDK 21 (the test used Microsoft OpenJDK 21.0.12.1 ).

```powershell
java -cp aspectjtools-1.9.22.jar org.aspectj.tools.ajc.Main -version
java -cp aspectjtools-1.9.22.jar org.aspectj.tools.ajc.Main -17 -classpath aspectjrt-1.9.22.jar -d build HelloWorld.java Greeting.aj
java -cp "build;aspectjrt-1.9.22.jar" HelloWorld
```

On Linux/macOS replace `;` with `:` in classpath.
`build` out of the files to be delivered. `ajc` compiles both sources and
apply the weaving; the Java `greet` method is empty, so the observed print
It comes from the AspectJ advice in `Greeting.aj`. You don't need a runtime agent.

## Expected result

ajc exit 0; programma exit 0, stdout esattamente Hello, World! seguito da newline e stderr vuoto.

## State of the test

syntax verified. behavior verified.

Source AspectJ .aj compiled and woven with ajc. The Java class has greeted empty: the result checks that the advice really produces greeting.

Actual Windows x64 test of 2026-10-08T11:01:56.068379+00:00: [log](verification/result.json).
The log includes hash SHA-256 of the source, observed versions, commands, exit codes, stdout and stderr.

## Primary sources

- [https://eclipse.dev/aspectj/doc/latest/devguide/ajc.html](https://eclipse.dev/aspectj/doc/latest/devguide/ajc.html)
- [https://eclipse.dev/aspectj/doc/latest/progguide/progguide.html](https://eclipse.dev/aspectj/doc/latest/progguide/progguide.html)
- [https://repo.maven.apache.org/maven2/org/aspectj/aspectjtools/1.9.22/](https://repo.maven.apache.org/maven2/org/aspectj/aspectjtools/1.9.22/)
- [https://repo.maven.apache.org/maven2/org/aspectj/aspectjrt/1.9.22/](https://repo.maven.apache.org/maven2/org/aspectj/aspectjrt/1.9.22/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.aj` | [Greeting.aj](Greeting.aj) verified |
