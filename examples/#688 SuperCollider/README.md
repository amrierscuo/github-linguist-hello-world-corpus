# #688 SuperCollider

Voce canonica `SuperCollider`, tipo `programming`, language_id `361`.

Valutare una stringa concatenata e postln in SuperCollider.

## Toolchain e riproduzione

Required genuine sclang compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede interpreter sclang e class library SuperCollider compatibile; nessuna sintesi audio necessaria per questo sorgente.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
sclang hello.scd
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Sorgente originale; interpreter/class library non configurati.

Requisiti residui:

- Required sclang toolchain and matching execution/format resources are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://doc.sccode.org/Classes/String.html](https://doc.sccode.org/Classes/String.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sc` | [hello.sc](variants/sc-4a5e9bf6/hello.sc) creato, verifiche pendenti |
| `.scd` | [hello.scd](hello.scd) creato, verifiche pendenti |
