# #332 Jasmin

Assemblare bytecode JVM con Jasmin e chiamare PrintStream.println.

Tipo canonico `programming`, language_id `180`.

Toolchain prevista: Jasmin 3.0.3 e JDK 21.

Dalla cartella dell’esempio:

```sh
java -cp "$JASMIN_CLASSPATH" jasmin.Main -d build Hello.j
java -cp build Hello
```

Risultato atteso: bytecode JVM valido; stdout Hello, World! e LF.

Il sorgente contiene istruzioni JVM esplicite. La classe assemblata rimane fuori dal corpus.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Jasmin 3.0.3 + CUP 0.9.2 + OpenJDK 21.0.12. [Log](verification/result.json). 

Fonti:

- [Jasmin — manuale originale](https://jasmin.sourceforge.net/guide.html)
- [Jasmin — progetto Sable](https://github.com/Sable/jasmin)

Classpath richiesto: `jasmin-3.0.3.jar`, `java_cup-0.9.2.jar`. I JAR originali sono disponibili da [Maven Central](https://repo.maven.apache.org/maven2/). Impostare la variabile di classpath del comando; separatore `;` su Windows, `:` su Unix.

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.j` | [Hello.j](Hello.j) verificato |
