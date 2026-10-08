# #539 Pkl

Voce canonica `Pkl`, tipo `programming`, language_id `288822799`.

Valutare una configurazione Pkl con string interpolation e serializzarla in JSON.

## Toolchain e riproduzione

Official Pkl Java evaluator — Pkl 0.32.1 (Windows 10.0, Java 21.0.12.1). Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Pkl Java CLI 0.32.1 ufficiale, checksum corrispondente all’asset jpkl della release Apple.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
java -jar /path/to/pkl-0.32.1.jar eval --format json hello.pkl
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

L’evaluator vero legge Pkl e produce name/message con valori esatti. Il formato Pickle della voce 0534 è distinto anche se l’estensione coincide.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://pkl-lang.org/main/current/pkl-cli/index.html](https://pkl-lang.org/main/current/pkl-cli/index.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pkl` | [hello.pkl](hello.pkl) verificato |
