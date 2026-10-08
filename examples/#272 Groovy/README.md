# #272 Groovy

Voce canonica `Groovy`, tipo `programming`, language_id `142`.

Interpolare una variabile in una GString Groovy e stamparla.

## Toolchain e riproduzione

Official Apache Groovy compiler/runtime jar — Groovy Version: 3.0.24 JVM: 21.0.12.1 Vendor: Microsoft OS: Windows 11. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Apache Groovy 3.0.24 ufficiale, JAR originale presente nella distribuzione Gradle 8.14.3; JDK 21. La prova invoca java -cp groovy-3.0.24.jar groovy.ui.GroovyMain hello.groovy.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
groovy hello.groovy
```

Risultato atteso: Exit 0; saluto esatto seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il compiler/runtime Groovy autentico analizza ed esegue il sorgente. Non è necessario un progetto Gradle per questa voce.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://groovy-lang.org/syntax.html#_string_interpolation](https://groovy-lang.org/syntax.html#_string_interpolation)
- [https://groovy-lang.org/](https://groovy-lang.org/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.groovy` | [hello.groovy](hello.groovy), [render.groovy](variants/ext-grt-2e677274/render.groovy), [render.groovy](variants/ext-gtpl-2e6774706c/render.groovy) creato, verifiche pendenti |
| `.grt` | [hello.grt](variants/ext-grt-2e677274/hello.grt) creato, verifiche pendenti |
| `.gtpl` | [hello.gtpl](variants/ext-gtpl-2e6774706c/hello.gtpl) creato, verifiche pendenti |
| `.gvy` | [hello.gvy](variants/ext-gvy-2e677679/hello.gvy) creato, verifiche pendenti |
