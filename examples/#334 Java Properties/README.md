# #334 Java Properties

Caricare un file Java Properties e leggere greeting con java.util.Properties.

Tipo canonico `data`, language_id `519377561`.

Toolchain prevista: JDK 21 java.util.Properties.

Dalla cartella dell’esempio:

```sh
java Verify.java
```

Risultato atteso: stdout Hello, World! e LF; property corretta.

Il file usa ASCII; nessuna ambiguità con la codifica storica di Properties.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: OpenJDK 21.0.12 Properties. [Log](verification/result.json). 

Fonti:

- [Java SE — Properties.load](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html#load(java.io.Reader))

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.properties` | [hello.properties](hello.properties) verificato |
