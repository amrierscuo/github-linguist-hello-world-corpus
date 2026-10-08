# #610 Redscript

Voce canonica `Redscript`, tipo `programming`, language_id `686691365`.

Definire una funzione Redscript originale che restituisce la stringa del saluto.

## Toolchain e riproduzione

Required genuine redscript compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede compiler jac3km4/redscript e runtime/librerie del gioco compatibili.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
redscript compile con i sorgenti hello.reds e il cache bundle/script resources del proprio Cyberpunk 2077; invocare CorpusGreeting.hello() nel relativo host.
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Funzione sorgente nel modulo originale; compiler/runtime game non disponibili. Non si deduce parsing dalla sintassi simile ad altri linguaggi.

Requisiti residui:

- Required redscript compiler/runtime and matching host resources are not available/configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://wiki.redmodding.org/redscript](https://wiki.redmodding.org/redscript)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.reds` | [hello.reds](hello.reds) creato, verifiche pendenti |
