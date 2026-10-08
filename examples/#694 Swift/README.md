# #694 Swift

Voce canonica `Swift`, tipo `programming`, language_id `362`.

Eseguire un sorgente Swift con string interpolation e print.

## Toolchain e riproduzione

Required genuine swift compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede toolchain Swift originale compatibile con il sistema.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
swift hello.swift
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Sorgente originale; compiler/runtime non disponibile.

Requisiti residui:

- Required swift toolchain and matching execution/format resources are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://docs.swift.org/swift-book/documentation/the-swift-programming-language/guidedtour/](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/guidedtour/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.swift` | [hello.swift](hello.swift) creato, verifiche pendenti |
