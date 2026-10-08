# #672 Smithy

Assemblare un modello Smithy e leggere il valore enum HELLO dal modello semantico.

Tipo canonico `programming`, language_id `1027892786`.

Toolchain prevista: JDK e Smithy model/utils.

Dalla cartella dell’esempio:

```sh
java -cp "$SMITHY_CLASSPATH" Verify.java
```

Risultato atteso: modello valido e enum Hello, World!.

L’obiettivo è il modello IDL, non un endpoint AWS o un client generato.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: JDK21 + Smithy model/utils 1.50.0. [Log](verification/result.json). 

Fonti:

- [Smithy IDL](https://smithy.io/2.0/spec/idl.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.smithy` | [hello.smithy](hello.smithy) verificato |
