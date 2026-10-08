# #453 Myghty

Voce canonica `Myghty`, tipo `programming`, language_id `239`.

Renderizzare una componente Myghty con parametro dichiarato nel blocco args.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede l’engine storico Myghty e una versione Python compatibile, secondo la sua API Interpreter.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
Configurare Myghty Interpreter con component_root della cartella e invocare hello.myt con name=World.
```

Risultato atteso: Hello, World!

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Componente originale; engine storico non configurato. Il nome è un parametro args e l’espressione lo inserisce nel corpo.

Requisiti residui:

- Historical Myghty template runtime/Python compatibility is not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://pythonhosted.org/Myghty/documentation.html](https://pythonhosted.org/Myghty/documentation.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.myt` | [hello.myt](hello.myt) creato, verifiche pendenti |
