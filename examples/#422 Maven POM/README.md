# #422 Maven POM

Interpretare un POM Maven, compilare un programma Java e creare un JAR con il saluto.

Tipo canonico `data`, language_id `226`.

Toolchain prevista: Apache Maven 3.9.x e JDK 21.

Dalla cartella dell’esempio:

```sh
mvn package
java -cp target/hello-world-1.0.0.jar corpus.Hello
```

Risultato atteso: Maven package riuscito; programma nel JAR stampa Hello, World! e LF.

Gli artifact e i plugin provengono da Maven Central. Il parametro corpus.build.directory permette isolare i file generati fuori dal corpus.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Apache Maven 3.9.9 + OpenJDK 21.0.12. [Log](verification/result.json). 

Fonti:

- [Apache Maven — POM reference](https://maven.apache.org/pom.html)
