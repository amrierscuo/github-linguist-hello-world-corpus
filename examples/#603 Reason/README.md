# #603 Reason

Voce canonica `Reason`, tipo `programming`, language_id `869538413`.

Compilare Reason e invocare print_endline dal programma originale.

## Toolchain e riproduzione

Original BuckleScript ReScript/Reason compiler with standard library — BuckleScript 9.0.2 ( Using OCaml:4.06.1+BS ). Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Frontend Reason di BuckleScript 9.0.2 autentico.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
bsc -I /path/to/bs-platform/lib/ocaml -bs-package-name corpus-greeting -bs-package-output commonjs:. -o Hello.cmj Hello.re; node Hello.js
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il frontend .re distinto legge sintassi Reason con terminatori e compila a JS; Node esegue il risultato e stampa il saluto esatto.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://reasonml.github.io/docs/en/quickstart-javascript](https://reasonml.github.io/docs/en/quickstart-javascript)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.re` | [Hello.re](Hello.re), [Hello.re](variants/rei-88fa759e/Hello.re) creato, verifiche pendenti |
| `.rei` | [Hello.rei](variants/rei-88fa759e/Hello.rei) creato, verifiche pendenti |
