# #681 Standard ML

Voce canonica `Standard ML`, tipo `programming`, language_id `357`.

Compilare ed eseguire un sorgente Standard ML con concatenazione e print.

## Toolchain e riproduzione

Original Poly/ML Standard ML compiler/interpreter — Poly/ML 5.7.1 Release. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Poly/ML 5.7.1 autentico Ubuntu, estratto sotto work.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
poly --script hello.sml
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Compiler/interpreter originali, stdout esatto e termine normale.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.polyml.org/documentation/](https://www.polyml.org/documentation/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ml` | [hello.ml](variants/ml-88c80c27/hello.ml) creato, verifiche pendenti |
| `.fun` | [hello.fun](variants/fun-28c9c936/hello.fun) creato, verifiche pendenti |
| `.sig` | [hello.sig](variants/sig-21be57d9/hello.sig) creato, verifiche pendenti |
| `.sml` | [hello.sml](hello.sml), [main.sml](variants/sig-21be57d9/main.sml) creato, verifiche pendenti |
