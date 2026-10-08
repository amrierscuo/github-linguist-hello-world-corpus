# #026 Alloy

Voce canonica: `Alloy`, tipo `programming`, `language_id: 13`.
`hello.als` vincola un'unica `Greeting` ad avere il testo `Hello, World!`,
richiede un'istanza con `run showGreeting` e controlla l'asserzione sul testo
con `check GreetingIsHelloWorld`, entrambi entro scope 3.

## Toolchain e riproduzione

Verificato su Windows x64 con **Alloy 6.2.0**, solver **SAT4J** incluso e
**Microsoft OpenJDK 21.0.12.1**. È necessario un JDK per il lancio del sorgente Java.
Scaricare il JAR ufficiale Maven Central nella directory locale `.tools`, poi:

```powershell
java -version
java -jar .tools/alloy-6.2.0.jar version
java -jar .tools/alloy-6.2.0.jar commands hello.als
java -Dorg.slf4j.simpleLogger.defaultLogLevel=error --class-path .tools/alloy-6.2.0.jar AlloyCheck.java hello.als
```

Artefatto Maven: `org.alloytools:org.alloytools.alloy.dist:6.2.0`.
Il JAR si chiama `org.alloytools.alloy.dist-6.2.0.jar` alla fonte; rinominarlo
localmente `alloy-6.2.0.jar` per i comandi sopra. SHA-256 verificato nel log:
`6037cbeee0e8423c1c468447ed10f5fcf2f2743a2ffc39cb1c81f2905c0fdb9d`.

`AlloyCheck.java` è un harness originale: delega parsing, typecheck, traduzione
e soluzione alle API Alloy ufficiali. Risultato atteso: `showGreeting: SAT` con
unico atomo stringa `"Hello, World!"`, `GreetingIsHelloWorld: UNSAT counterexample,
scope 3`, e `PASS` per tutte le asserzioni. Include un controllo negativo della
firma malformata rifiutata dal parser reale.

## Stato ed evidenza

Artefatto creato; sintassi **verificata**; semantica **verificata** con SAT4J.
L'assenza di controesempi è attestata entro lo scope specificato, non oltre i
limiti della ricerca. La valutazione del campo controlla la stringa dell'istanza
effettiva. Il precedente `exec` CLI aveva terminato senza produrre una receipt;
il solo codice 0 di quel comando non è stato usato come prova semantica.
Nessun requisito residuo per la verifica entro scope 3.

Log: [alloy.json](verification/alloy.json), con comandi, output delle API,
versione e SHA-256 degli artefatti. `path_normalization` documenta i percorsi
normalizzati; i sorgenti e i risultati del solver restano invariati.

## Fonti ufficiali

- [Documentazione e API Alloy](https://alloytools.org/documentation.html).
- [Distribuzione e requisiti](https://github.com/AlloyTools/org.alloytools.alloy).
- [JAR ufficiale Maven Central 6.2.0](https://repo.maven.apache.org/maven2/org/alloytools/org.alloytools.alloy.dist/6.2.0/).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.als` | [hello.als](hello.als) verificato |
