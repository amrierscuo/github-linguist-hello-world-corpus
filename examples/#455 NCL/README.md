# #455 NCL

Voce canonica `NCL`, tipo `programming`, language_id `240`.

Stampare una stringa concatenata nel linguaggio NCAR NCL.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede NCL e le librerie scientifiche NCAR compatibili. -Q sopprime il banner, -n sopprime l’indice nelle stringhe stampate.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
ncl -Q -n hello.ncl
```

Risultato atteso: Hello, World!

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Programma originale; runtime non configurato.

Requisiti residui:

- NCAR NCL interpreter and runtime libraries are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.ncl.ucar.edu/Document/Functions/Built-in/print.shtml](https://www.ncl.ucar.edu/Document/Functions/Built-in/print.shtml)
- [https://www.ncl.ucar.edu/Document/Manuals/Ref_Manual/NclStatements.shtml](https://www.ncl.ucar.edu/Document/Manuals/Ref_Manual/NclStatements.shtml)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ncl` | [hello.ncl](hello.ncl) creato, verifiche pendenti |
