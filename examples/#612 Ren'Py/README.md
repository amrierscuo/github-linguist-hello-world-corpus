# #612 Ren'Py

Voce canonica `Ren'Py`, tipo `programming`, language_id `322`.

Mostrare il saluto come dialogo nel punto start di un progetto Ren’Py originale.

## Toolchain e riproduzione

Required genuine renpy compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede Ren’Py SDK compatibile e progetto nella directory corrente con game/script.rpy.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
renpy . lint; renpy .
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Sorgente originale label start e statement dialogo, non commento. SDK/lint/display non configurati.

Requisiti residui:

- Required renpy compiler/runtime and matching host resources are not available/configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.renpy.org/doc/html/quickstart.html](https://www.renpy.org/doc/html/quickstart.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.rpy` | [script.rpy](game/script.rpy) creato, verifiche pendenti |
