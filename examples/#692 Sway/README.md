# #692 Sway

Voce canonica `Sway`, tipo `programming`, language_id `271471144`.

Restituire una stringa di 13 caratteri da uno script Sway originale.

## Toolchain e riproduzione

Required genuine forc compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede Fuel Sway compiler/forc e un runner locale compatibile, senza invio di transazioni.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
forc build; forc run --dry-run
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Sway indica il linguaggio Fuel, con str[13]; il programma non eÌâ‚¬ una configurazione del window manager omonimo. Toolchain assente.

Requisiti residui:

- Required forc toolchain and matching execution/format resources are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://fuellabs.github.io/sway/v0.31.0/basics/variables.html](https://fuellabs.github.io/sway/v0.31.0/basics/variables.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sw` | [main.sw](src/main.sw) creato, verifiche pendenti |
