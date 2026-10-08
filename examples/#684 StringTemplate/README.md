# #684 StringTemplate

Voce canonica `StringTemplate`, tipo `markup`, language_id `89855901`.

Compilare/renderizzare un template StringTemplate con parametro name.

## Toolchain e riproduzione

Official StringTemplate Java compiler/renderer — ST4 4.3.4 / ANTLR runtime 3.5.3. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

StringTemplate Java 4.3.4 originale e ANTLR runtime 3.5.3, Java21. Su Linux il separatore classpath eÌâ‚¬ : invece di ;.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
java -cp /path/to/ST4-4.3.4.jar;/path/to/antlr-runtime-3.5.3.jar Verify.java
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il vero ST compiler/renderer produce World e Reader; il confronto ignora soltanto lo spazio ai bordi del rendering.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.stringtemplate.org/](https://www.stringtemplate.org/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.st` | [hello.st](hello.st) verificato |
