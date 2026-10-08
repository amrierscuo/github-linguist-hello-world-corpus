# #747 Velocity Template Language

Renderizzare Velocity Template Language con parametro target.

Tipo canonico `markup`, language_id `292377326`.

Toolchain prevista: JDK e Apache Velocity engine.

Dalla cartella dell’esempio:

```sh
java -cp "$VELOCITY_CLASSPATH" Verify.java
```

Risultato atteso: output esatto Hello, World! e newline.

Il motore Apache interpreta il riferimento $target.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: JDK21 + Apache Velocity2.4.1/CommonsLang3.17/SLF4J2.0.16. [Log](verification/result.json). 

Fonti:

- [Apache Velocity VTL](https://velocity.apache.org/engine/2.4.1/user-guide.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.vtl` | [hello.vtl](hello.vtl) verificato |
