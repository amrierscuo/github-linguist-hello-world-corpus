# #601 ReScript

Voce canonica `ReScript`, tipo `programming`, language_id `501875647`.

Compilare ReScript con binding locale e Js.log, poi eseguire il JavaScript genuino.

## Toolchain e riproduzione

Original BuckleScript ReScript/Reason compiler with standard library — BuckleScript 9.0.2 ( Using OCaml:4.06.1+BS ). Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

BuckleScript/ReScript 9.0.2 autentico con libreria OCaml della stessa distribuzione. Progetto bsconfig.json originale.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
bsc -I /path/to/bs-platform/lib/ocaml -bs-package-name corpus-greeting -bs-package-output commonjs:. -o Hello.cmj Hello.res; node Hello.js
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il frontend .res autentico compila in JS, eseguito da Node. La prova usa il binario Linux con cwd di progetto per la risoluzione bsconfig.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://rescript-lang.org/docs/manual/v9.0.0/overview](https://rescript-lang.org/docs/manual/v9.0.0/overview)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.res` | [Hello.res](Hello.res), [Hello.res](variants/resi-1bac9c18/Hello.res) creato, verifiche pendenti |
| `.resi` | [Hello.resi](variants/resi-1bac9c18/Hello.resi) creato, verifiche pendenti |
