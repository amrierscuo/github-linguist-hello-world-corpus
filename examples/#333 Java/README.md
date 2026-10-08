# #333 Java

Compilare ed eseguire una classe Java con metodo main.

Tipo canonico `programming`, language_id `181`.

Toolchain prevista: Microsoft OpenJDK 21.

Dalla cartella dell’esempio:

```sh
javac -d build Hello.java
java -cp build Hello
```

Risultato atteso: stdout Hello, World! e LF, uscita 0.

Il controllo esegue il bytecode compilato con javac.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: OpenJDK 21.0.12. [Log](verification/result.json). 

Fonti:

- [Oracle — Java main e primo programma](https://docs.oracle.com/javase/tutorial/getStarted/cupojava/win32.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.java` | [Hello.java](Hello.java) verificato |
| `.jav` | [hello.jav](variants/jav-220a15e8/hello.jav) creato, verifiche pendenti |
| `.jsh` | [hello.jsh](variants/jsh-e38b41dc/hello.jsh) creato, verifiche pendenti |
