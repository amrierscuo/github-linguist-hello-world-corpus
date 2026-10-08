# #345 Jsonnet

Voce canonica `Jsonnet`, tipo `programming`, language_id `664885656`.

Valutare un oggetto Jsonnet con binding locale e stringa concatenata.

## Toolchain e riproduzione

Official Jsonnet C++ compiler/evaluator — Jsonnet commandline interpreter v0.20.0. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Jsonnet C++ 0.20.0 ufficiale dal pacchetto Ubuntu, estratto sotto work senza installazione globale.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
jsonnet hello.jsonnet
```

Risultato atteso: JSON esatto {"message":"Hello, World!"}; exit 0.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il vero evaluator produce JSON; la verifica legge quel prodotto e confronta esattamente il campo message.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://jsonnet.org/learning/tutorial.html](https://jsonnet.org/learning/tutorial.html)
- [https://jsonnet.org/ref/spec.html](https://jsonnet.org/ref/spec.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.jsonnet` | [hello.jsonnet](hello.jsonnet), [driver.jsonnet](variants/libsonnet-cf82fe81/driver.jsonnet) creato, verifiche pendenti |
| `.libsonnet` | [hello.libsonnet](variants/libsonnet-cf82fe81/hello.libsonnet) creato, verifiche pendenti |
