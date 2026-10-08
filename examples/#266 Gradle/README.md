# #266 Gradle

Voce canonica `Gradle`, tipo `data`, language_id `136`.

Registrare un task Gradle nel Groovy DSL e stamparne il saluto durante doLast.

## Toolchain e riproduzione

Official Gradle distribution Groovy DSL — 8.14.3; JDK 21. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Distribuzione Gradle ufficiale 8.14.3 con JDK 21. Il progetto non usa plugin esterni o repository. Eseguire in copia con GRADLE_USER_HOME isolata.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
gradle --no-daemon --offline --console=plain --max-workers=1 -q hello
```

Risultato atteso: Exit 0; Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il launcher ufficiale configura settings.gradle e build.gradle, registra hello e ne esegue l’azione. La prova termina 0 con stdout esatto.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://docs.gradle.org/8.14.3/userguide/tutorial_using_tasks.html](https://docs.gradle.org/8.14.3/userguide/tutorial_using_tasks.html)
- [https://docs.gradle.org/8.14.3/userguide/writing_build_scripts.html](https://docs.gradle.org/8.14.3/userguide/writing_build_scripts.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gradle` | [build.gradle](build.gradle), [settings.gradle](settings.gradle) verificato |
