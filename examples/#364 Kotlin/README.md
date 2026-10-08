# #364 Kotlin

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Compilare Kotlin/JVM e stampare Hello, World!.

La funzione main usa una val e interpolazione di stringa. La prova invoca il compiler JVM ufficiale e la JVM, con jar generato soltanto in work.

## Toolchain e riproduzione

Kotlin2.4.21, OpenJDK21 Microsoft

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
kotlinc Hello.kt -include-runtime -d hello.jar
```

```text
java -jar hello.jar
```

## Risultato atteso e stato

stdout esattamente Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://kotlinlang.org/docs/command-line.html
- https://github.com/JetBrains/kotlin/releases/tag/v2.4.21

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.kt` | [Hello.kt](Hello.kt) verificato |
| `.ktm` | [hello.ktm](variants/ktm-5ead4c6e/hello.ktm) creato, verifiche pendenti |
| `.kts` | [hello.kts](variants/kts-f3ce7309/hello.kts) creato, verifiche pendenti |
