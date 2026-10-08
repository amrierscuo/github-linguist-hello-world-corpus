# #524 Pan

Voce canonica `Pan`, tipo `programming`, language_id `276`.

Compilare un object template Pan e ottenere una configurazione JSON con message.

## Toolchain e riproduzione

Official Quattor Pan compiler — pan compiler version: 10.8. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Quattor Pan 10.8 ufficiale. Il fat JAR ha Main-Class Compiler che stampa solo la versione; il vero CLI è pan_compiler, usato nella prova.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
java -cp /path/to/panc-10.8.jar org.quattor.pan.pan_compiler --formats json --output-dir build greeting.pan
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il compiler autentico genera greeting.json con message esatto Hello, World!.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://quattor-pan.readthedocs.io/en/latest/pan-book/pan-book.html](https://quattor-pan.readthedocs.io/en/latest/pan-book/pan-book.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pan` | [greeting.pan](greeting.pan) verificato |
