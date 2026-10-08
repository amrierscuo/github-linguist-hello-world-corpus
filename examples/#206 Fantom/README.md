# #206 Fantom

Voce canonica `Fantom`, tipo `programming`, language_id `110`.

Compilare lo script Fantom Hello e concatenare il saluto nel metodo main.

## Toolchain e riproduzione

Official Fantom JVM distribution — 1.0.83. Ambiente della prova: **Windows x64**.

Distribuzione portable Fantom 1.0.83 con JVM. La prova usa direttamente java -Dfan.home=<fantom> -cp <fantom>/lib/java/sys.jar fanx.tools.Fan hello.fan. Il log conserva il comando effettivo e l’hash del JAR.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
fan hello.fan
```

Risultato atteso: Exit 0; stdout esattamente Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il comando -version Fantom restituisce codice 3 nella distribuzione usata, pur riportando la versione completa; l’esecuzione del sorgente termina 0 e produce il saluto esatto.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sorgenti verificati in staging. I soli probe di disponibilità non attestano parsing
o esecuzione. Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://fantom.org/](https://fantom.org/)
- [https://github.com/fantom-lang/fantom/releases/tag/v1.0.83](https://github.com/fantom-lang/fantom/releases/tag/v1.0.83)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.fan` | [hello.fan](hello.fan) verificato |
