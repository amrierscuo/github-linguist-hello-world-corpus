# #533 Pic

Voce canonica `Pic`, tipo `markup`, language_id `425`.

Disegnare un box etichettato dal preprocessore Pic e renderizzarlo in testo.

## Toolchain e riproduzione

Genuine GNU Pic and groff ASCII renderer — GNU pic (groff) version 1.23.0. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

GNU Pic/groff 1.23.0 autentici.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
pic hello.pic; groff -p -Tascii hello.pic
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Pic genera le primitive troff; groff rende un box con testo Hello, World!. Un warning di grotty sullo spessore della linea non impedisce il rendering.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.gnu.org/software/groff/manual/groff.html#Pictures](https://www.gnu.org/software/groff/manual/groff.html#Pictures)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pic` | [hello.pic](hello.pic) verificato |
| `.chem` | [hello.chem](variants/chem-e7e80156/hello.chem) creato, verifiche pendenti |
