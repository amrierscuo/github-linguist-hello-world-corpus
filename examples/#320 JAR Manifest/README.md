# #320 JAR Manifest

Use an authentic JAR Manifest to start the class that prints greeting.

## Toolchain

Microsoft OpenJDK java/javac/jar 21.0.12.1

## Commands and procedure

javac -d build Hello.java VerifyManifest.java; java -cp build VerifyManifest MANIFEST.MF; jar --create --file build/hello.jar --manifest MANIFEST.MF -C Hello.class; java -jar build/hello.jar

## Expected result

java.util.jar.Manifest reads three correct attributes; JAR starts Hello and Hello, World! print, exit 0.

## Status

syntax and behavior verified.

MANIFEST.MF originale usa CRLF e riga vuota finale. Il tool jar e il launcher leggono davvero Main-Class; attributo custom Corpus-Greeting conserva il testo. Solo sorgenti e manifest vengono consegnati, nessuna classe/JAR binaria.

Actual verification of 2026-10-08T12:30:00.202779+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://docs.oracle.com/en/java/javase/21/docs/specs/jar/jar.html](https://docs.oracle.com/en/java/javase/21/docs/specs/jar/jar.html)
- [https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/jar/Manifest.html](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/jar/Manifest.html)
