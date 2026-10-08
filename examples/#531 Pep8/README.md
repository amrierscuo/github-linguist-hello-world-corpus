# #531 Pep8

Voce canonica `Pep8`, tipo `programming`, language_id `840372442`.

Stampare una stringa terminata da zero nel simulatore educativo Pep/8.

## Toolchain e riproduzione

Required genuine compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede l’assembler/simulatore Pep/8 e il relativo OS, non Pep/9 o una CPU diversa.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
Aprire hello.pep nel software Pep/8 ufficiale, Assemble, poi Run con il suo OS standard.
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Sorgente originale STRO direct, STOP e dati ASCII dopo il codice; strumenti non disponibili.

Requisiti residui:

- Required pep8 compiler/interpreter and matching host libraries are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.computersystemsbook.com/4th-edition/pep8/](https://www.computersystemsbook.com/4th-edition/pep8/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pep` | [hello.pep](hello.pep) creato, verifiche pendenti |
