# #535 PicoLisp

Voce canonica `PicoLisp`, tipo `programming`, language_id `285`.

Stampare il saluto con prinl e uscire dal processo PicoLisp.

## Toolchain e riproduzione

Authentic PicoLisp native interpreter — 23.12-1build2. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

PicoLisp 23.12-1build2 autentico Ubuntu estratto sotto work.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
picolisp hello.l
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Interpreter vero, exit 0 e saluto esatto; sono usate soltanto primitive native.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://software-lab.de/doc/refP.html#prinl](https://software-lab.de/doc/refP.html#prinl)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.l` | [hello.l](hello.l) verificato |
