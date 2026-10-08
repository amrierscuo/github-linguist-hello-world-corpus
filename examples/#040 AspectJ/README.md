# #040 AspectJ

Stampare Hello, World! da un advice AspectJ before, applicato all'esecuzione del metodo Java HelloWorld.greet tramite weaving in compilazione.

## File

- `Greeting.aj`
- `HelloWorld.java`

## Toolchain e verifica

AspectJ ajc/aspectjrt 1.9.22; Microsoft OpenJDK 21.0.12.1; sorgenti e bytecode Java 17.

Scaricare `aspectjtools-1.9.22.jar` e `aspectjrt-1.9.22.jar` dalle directory
Maven ufficiali indicate sotto; collocarli in una cartella di tool esterna al
corpus. I comandi seguenti usano percorsi relativi per semplicità: adattarli
alla posizione effettiva dei JAR. Eseguire dalla cartella dell'esempio con
JDK 21 (il test ha usato Microsoft OpenJDK 21.0.12.1).

```powershell
java -cp aspectjtools-1.9.22.jar org.aspectj.tools.ajc.Main -version
java -cp aspectjtools-1.9.22.jar org.aspectj.tools.ajc.Main -17 -classpath aspectjrt-1.9.22.jar -d build HelloWorld.java Greeting.aj
java -cp "build;aspectjrt-1.9.22.jar" HelloWorld
```

Su Linux/macOS sostituire `;` con `:` nel classpath. Conservare la directory
`build` fuori dai file da consegnare. `ajc` compila entrambi i sorgenti e
applica il weaving; il metodo Java `greet` è vuoto, quindi la stampa osservata
proviene dall'advice AspectJ in `Greeting.aj`. Non serve un agente runtime.

## Risultato atteso

ajc exit 0; programma exit 0, stdout esattamente Hello, World! seguito da newline e stderr vuoto.

## Stato della prova

Sintassi verificata. Semantica verificata.

Sorgente AspectJ .aj compilata e intrecciata con ajc. La classe Java ha greet vuoto: il risultato verifica che l'advice produca realmente il saluto.

Prova effettiva Windows x64 del 2026-10-08T11:01:56.068379+00:00: [log](verification/result.json).
Il log include hash SHA-256 della sorgente, versioni osservate, comandi, codici di uscita, stdout e stderr.

## Fonti primarie

- [https://eclipse.dev/aspectj/doc/latest/devguide/ajc.html](https://eclipse.dev/aspectj/doc/latest/devguide/ajc.html)
- [https://eclipse.dev/aspectj/doc/latest/progguide/progguide.html](https://eclipse.dev/aspectj/doc/latest/progguide/progguide.html)
- [https://repo.maven.apache.org/maven2/org/aspectj/aspectjtools/1.9.22/](https://repo.maven.apache.org/maven2/org/aspectj/aspectjtools/1.9.22/)
- [https://repo.maven.apache.org/maven2/org/aspectj/aspectjrt/1.9.22/](https://repo.maven.apache.org/maven2/org/aspectj/aspectjrt/1.9.22/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.aj` | [Greeting.aj](Greeting.aj) verificato |
