# #336 Java Template Engine

Compilare un template JTE Java con parametro target e renderizzare il saluto.

Tipo canonico `programming`, language_id `599494012`.

Toolchain prevista: JDK 21, jte e jte-runtime 3.1.16.

Dalla cartella dell’esempio:

```sh
java -cp "$JTE_CLASSPATH" Verify.java build/jte
```

Risultato atteso: stdout Hello, World! e LF, uscita 0.

Il motore compila il template in Java con la toolchain JDK, poi renderizza il parametro costante.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: OpenJDK 21.0.12 + jte/jte-runtime 3.1.16. [Log](verification/result.json). 

Fonti:

- [JTE — sintassi](https://jte.gg/syntax/)
- [JTE — implementazione](https://github.com/casid/jte)

Classpath richiesto: `jte-3.1.16.jar`, `jte-runtime-3.1.16.jar`, `jte-extension-api-3.1.16.jar`. I JAR originali sono disponibili da [Maven Central](https://repo.maven.apache.org/maven2/). Impostare la variabile di classpath del comando; separatore `;` su Windows, `:` su Unix.

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.jte` | [hello.jte](hello.jte) verificato |
