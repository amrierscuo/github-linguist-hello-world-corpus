# #685 Stylus

Voce canonica `Stylus`, tipo `markup`, language_id `359`.

Compilare Stylus in una regola CSS content che contiene il saluto.

## Toolchain e riproduzione

Official stylus compiler/parser — 0.64.0. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Compiler Stylus 0.64.0 autentico.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
npm install --prefix .tools stylus@0.64.0; node verify.cjs .tools build
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il CSS generato contiene selector e content corretti. Ambito semantico: generazione CSS, non visualizzazione browser.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://stylus-lang.com/docs/](https://stylus-lang.com/docs/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.styl` | [hello.styl](hello.styl) verificato |
