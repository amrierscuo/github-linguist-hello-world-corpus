# #320 JAR Manifest

Usare un JAR Manifest autentico per avviare la classe che stampa il saluto.

## Toolchain

Microsoft OpenJDK java/javac/jar 21.0.12.1

## Comandi e procedura

javac -d build Hello.java VerifyManifest.java; java -cp build VerifyManifest MANIFEST.MF; jar --create --file build/hello.jar --manifest MANIFEST.MF -C build Hello.class; java -jar build/hello.jar

## Risultato atteso

java.util.jar.Manifest legge tre attributi corretti; il JAR avvia Hello e stampa Hello, World!, exit 0.

## Stato

Sintassi e semantica verificate.

MANIFEST.MF originale usa CRLF e riga vuota finale. Il tool jar e il launcher leggono davvero Main-Class; attributo custom Corpus-Greeting conserva il testo. Solo sorgenti e manifest vengono consegnati, nessuna classe/JAR binaria.

Verifica effettiva del 2026-10-08T12:30:00.202779+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://docs.oracle.com/en/java/javase/21/docs/specs/jar/jar.html](https://docs.oracle.com/en/java/javase/21/docs/specs/jar/jar.html)
- [https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/jar/Manifest.html](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/jar/Manifest.html)
