# #263 Golo

Voce canonica `Golo`, tipo `programming`, language_id `133`.

Compilare ed eseguire un modulo Golo con main, binding locale e concatenazione.

## Toolchain e riproduzione

Official Eclipse Golo compiler and JVM runtime — 3.4.0. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Eclipse Golo 3.4.0 portable e JDK 21. La prova richiama org.eclipse.golo.cli.Main con il classpath dei JAR della distribuzione originale.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
golo check --files hello.golo; golo golo --files hello.golo
```

Risultato atteso: Entrambi i comandi exit 0; esecuzione stampa il saluto esatto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Check e compilazione al volo sono eseguiti dal compiler originale Eclipse. Il file termina con newline, significativo per la sintassi Golo.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://golo-lang.org/](https://golo-lang.org/)
- [https://golo-lang.github.io/documentation/next/](https://golo-lang.github.io/documentation/next/)
- [https://github.com/eclipse-archived/golo-lang](https://github.com/eclipse-archived/golo-lang)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.golo` | [hello.golo](hello.golo) verificato |
