# #536 PigLatin

Voce canonica `PigLatin`, tipo `programming`, language_id `286`.

Caricare un TSV locale e trasformare World in un record PigLatin con il saluto.

## Toolchain e riproduzione

Required genuine compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede Apache Pig 0.17.0 e runtime Java/Hadoop compatibili per execution local.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
pig -x local hello.pig
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

LOAD, FOREACH GENERATE e CONCAT originali. DUMP deve mostrare (Hello, World!); toolchain locale non configurata.

Requisiti residui:

- Required pig compiler/interpreter and matching host libraries are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://pig.apache.org/docs/r0.17.0/basic.html](https://pig.apache.org/docs/r0.17.0/basic.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pig` | [hello.pig](hello.pig) creato, verifiche pendenti |
