# #690 Survex data

Voce canonica `Survex data`, tipo `data`, language_id `24470517`.

Processare una misura Survex originale e leggere titolo e stazioni dal suo modello 3d.

## Toolchain e riproduzione

Official Survex Cavern survey processor and dump3d reader — <workspace>/work/tools_681_700/linux/usr/bin/cavern - Survex 1.4.4. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Survex 1.4.4 autentico e PROJ9.4 locale. PRoot5.1.0 mappa solo nella vista del processo i message files estratti sotto /usr/share/survex, senza installazione o scrittura globale.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
cavern -o build/hello.3d hello.svx; dump3d build/hello.3d
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il titolo Hello, World! eÌâ‚¬ metadata della survey; i dati contengono un ingresso fissato e una camera misurata. Cavern e dump3d autentici producono/leggono il modello.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://survex.com/docs/manual/cavern.htm](https://survex.com/docs/manual/cavern.htm)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.svx` | [hello.svx](hello.svx) verificato |
