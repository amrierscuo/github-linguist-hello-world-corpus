# #267 Gradle Kotlin DSL

Voce canonica `Gradle Kotlin DSL`, tipo `data`, language_id `432600901`.

Registrare ed eseguire un task Gradle nel Kotlin DSL usando una val interpolata.

## Toolchain e riproduzione

Official Gradle distribution Kotlin DSL — 8.14.3; JDK 21. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Gradle ufficiale 8.14.3, Kotlin incorporato 2.0.21 e JDK 21. Non servono plugin Kotlin scaricati. Eseguire in una copia di lavoro con cache Gradle isolata.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
gradle --no-daemon --offline --console=plain --max-workers=1 -q hello
```

Risultato atteso: Task hello exit 0; saluto esatto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

build.gradle.kts e settings.gradle.kts sono realmente compilati dal Kotlin DSL Gradle; non sono eseguiti come una normale applicazione Kotlin.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://docs.gradle.org/8.14.3/userguide/kotlin_dsl.html](https://docs.gradle.org/8.14.3/userguide/kotlin_dsl.html)
- [https://docs.gradle.org/8.14.3/userguide/tutorial_using_tasks.html](https://docs.gradle.org/8.14.3/userguide/tutorial_using_tasks.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gradle.kts` | [build.gradle.kts](build.gradle.kts), [settings.gradle.kts](settings.gradle.kts) verificato |
