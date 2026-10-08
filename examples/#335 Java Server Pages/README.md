# #335 Java Server Pages

Renderizzare una pagina JSP che restituisce Hello, World! come testo.

Tipo canonico `programming`, language_id `182`.

Toolchain prevista: Apache Tomcat con Jasper JSP compiler e runtime Servlet.

Dalla cartella dell’esempio:

```sh
java -cp "$TOMCAT_CLASSPATH" Verify.java build/tomcat
```

Risultato atteso: HTTP 200, content-type text/plain, corpo Hello, World! seguito da newline.

La direttiva page e l’espressione JSP richiedono Jasper; un parser HTML generico non ne verifica la compilazione.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: OpenJDK 21.0.12 + Apache Tomcat/Jasper 10.1.42 + ECJ 3.33.0. [Log](verification/result.json). 

Fonti:

- [Apache Tomcat — Jasper JSP engine](https://tomcat.apache.org/tomcat-10.1-doc/jasper-howto.html)

Il checker avvia Tomcat soltanto su 127.0.0.1 e una porta assegnata dal sistema, richiede la pagina, controlla corpo e Content-Type e arresta/distrugge il server in finally. I file Jasper generati vanno in build/tomcat.

Classpath: tomcat-embed-core, tomcat-embed-el e tomcat-embed-jasper 10.1.42; ecj 3.33.0; jakarta.annotation-api 2.1.1. Artifact originali da Maven Central. Su Windows separare i JAR con punto e virgola, su Unix con due punti.

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.jsp` | [hello.jsp](hello.jsp), [hello.jsp](variants/tag-2e34b808/hello.jsp) creato, verifiche pendenti |
| `.tag` | [hello.tag](variants/tag-2e34b808/hello.tag) creato, verifiche pendenti |
