# #776 Wollok

Voce canonica `Wollok`, tipo `programming`, language_id `632745969`.

Oggetto Wollok originale greeting con metodo hello(), importato da un programma che invia il risultato a console.println.

## Toolchain e riproduzione

wollok-ts / Node.js 22.20.0 — 4.3.0. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Node.js 22.20.0 e wollok-ts 4.3.0 del progetto Uqbar. Installare il pacchetto in un prefisso esterno e impostare NODE_PATH sul relativo node_modules.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
node verify.cjs
```

Risultato atteso: Hello, World! prodotto dal programma e PASS.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il parser originale analizza entrambi i sorgenti, buildEnvironment li collega con WRE e l’interprete originale esegue il programma. Il driver raccoglie il log della console dell’interprete e lo confronta con il saluto.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://uqbar-project.github.io/wollok-ts/](https://uqbar-project.github.io/wollok-ts/)
- [https://github.com/uqbar-project/wollok-ts](https://github.com/uqbar-project/wollok-ts)
- [https://www.wollok.org/](https://www.wollok.org/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.wlk` | [greeting.wlk](greeting.wlk) verificato |
