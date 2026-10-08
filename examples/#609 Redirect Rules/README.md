# #609 Redirect Rules

Voce canonica `Redirect Rules`, tipo `data`, language_id `1020148948`.

Leggere una regola Netlify che riscrive il percorso hello su un file locale con il saluto.

## Toolchain e riproduzione

Official Netlify Redirect Parser — 16.1.1. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Parser Netlify ufficiale 16.1.1, Node 22.20.0.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
npm install --prefix .tools @netlify/redirect-parser@16.1.1; node verify.cjs .tools
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

parseAllRedirects valida e normalizza _redirects; il helper controlla from/to/status e il dato del target. Ambito: parsing e risoluzione locale, senza deploy o serving HTTP.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://docs.netlify.com/manage/routing/redirects/overview/](https://docs.netlify.com/manage/routing/redirects/overview/)
