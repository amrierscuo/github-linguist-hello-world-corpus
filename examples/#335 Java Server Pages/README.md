# #335 Java Server Pages

Render a JSP page that returns Hello, World! as text.

Canonical type `programming`, language_id `182`.

Suggested toolchain: Apache Tomcat with Jasper JSP compiler and runtime Servlet.

From the example directory:

```sh
java -cp "$TOMCAT_CLASSPATH" Verify.java build/tomcat
```

Expected result: HTTP 200, content-type text/plain, body Hello, World! followed by newline.

The JSP directive and expression require Jasper; a generic parser HTML does not verify its compilation.

Recorded status: syntax verified; behavior verified. Toolchain: OpenJDK 21.0.12 + Apache Tomcat/Jasper 10.1.42 + ECJ 3.33.0. [Log](verification/result.json).

Sources:

- [Apache Tomcat — Jasper JSP engine](https://tomcat.apache.org/tomcat-10.1-doc/jasper-howto.html)

Il checker avvia Tomcat soltanto su 127.0.0.1 e una porta assegnata dal sistema, richiede la pagina, controlla corpo e Content-Type e arresta/distrugge il server in finally. I file Jasper generati vanno in build/tomcat.

Classpath: tomcat-embed-core, tomcat-embed-el e tomcat-embed-jasper 10.1.42; ecj 3.33.0; jakarta.annotation-api 2.1.1. Artifact originali da Maven Central. Su Windows separare i JAR con punto e virgola, su Unix con due punti.

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.jsp` | [hello.jsp](hello.jsp), [hello.jsp](variants/tag-2e34b808/hello.jsp) created; verification pending |
| `.tag` | [hello.tag](variants/tag-2e34b808/hello.tag) created; verification pending |
