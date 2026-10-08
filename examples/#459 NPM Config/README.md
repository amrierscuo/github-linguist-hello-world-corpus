# #459 NPM Config

Voce canonica `NPM Config`, tipo `data`, language_id `685022663`.

Leggere il valore Hello, World! dalla configurazione NPM locale del progetto.

## Toolchain e riproduzione

Actual NPM project npmrc parser/config reader — 11.14.1. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

NPM reale 11.14.1. Copiare .npmrc in un progetto temporaneo con package.json private e usare due file config vuoti per isolare il progetto.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
npm --userconfig /path/to/empty-user.npmrc --globalconfig /path/to/empty-global.npmrc config get init-author-name
```

Risultato atteso: Hello, World!

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il parser/config reader NPM legge init-author-name e audit=false. Nessun pacchetto installato, nessuna modifica alle configurazioni utente/globali.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://docs.npmjs.com/cli/v11/configuring-npm/npmrc](https://docs.npmjs.com/cli/v11/configuring-npm/npmrc)
- [https://docs.npmjs.com/cli/v11/using-npm/config#init-author-name](https://docs.npmjs.com/cli/v11/using-npm/config#init-author-name)
