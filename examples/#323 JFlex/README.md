# #323 JFlex

Generare un lexer Java con JFlex e riconoscere World per stampare Hello, World!.

Tipo canonico `programming`, language_id `173`.

Toolchain prevista: JFlex 1.9.1, java-cup-runtime e JDK 21.

Dalla cartella dell’esempio:

```sh
java -cp "$JFLEX_CLASSPATH" jflex.Main -d build hello.jflex
javac -d build build/GreetingLexer.java
java -cp build GreetingLexer input.txt
```

Risultato atteso: uscita 0; stdout Hello, World! seguito da newline.

La parola World è l’input del lexer generato: l’output deriva dall’azione della regola, non da un parser di prova scritto ad hoc.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: JFlex 1.9.1 + CUP runtime 11b-20160615-3 + OpenJDK 21.0.12. [Log](verification/result.json). 

Fonti:

- [JFlex — manuale originale](https://jflex.de/manual.html)

Classpath richiesto: `jflex-1.9.1.jar`, `java-cup-runtime-11b-20160615-3.jar`. I JAR originali sono disponibili da [Maven Central](https://repo.maven.apache.org/maven2/). Impostare la variabile di classpath del comando; separatore `;` su Windows, `:` su Unix.

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.flex` | [hello.flex](variants/flex-1e75c1a3/hello.flex) creato, verifiche pendenti |
| `.jflex` | [hello.jflex](hello.jflex) verificato |
