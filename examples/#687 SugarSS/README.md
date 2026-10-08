# #687 SugarSS

Voce canonica `SugarSS`, tipo `markup`, language_id `826404698`.

Leggere SugarSS e serializzare la dichiarazione content in CSS.

## Toolchain e riproduzione

Official sugarss compiler/parser — 5.0.2. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Parser SugarSS e PostCSS originali, versioni loggate.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
npm install --prefix .tools sugarss postcss; node verify.cjs .tools build
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il parser autentico produce una dichiarazione AST content con valore esatto; PostCSS serializza CSS valido. Ambito: modello/stile compilato.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/postcss/sugarss](https://github.com/postcss/sugarss)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sss` | [hello.sss](hello.sss) verificato |
