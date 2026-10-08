# #618 Riot

Voce canonica `Riot`, tipo `markup`, language_id `878396783`.

Compilare e renderizzare una componente Riot parametrica.

## Toolchain e riproduzione

Official Riot component compiler and official SSR runtime — 9.4.6 / SSR 9. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Compiler Riot 9.4.6 e SSR ufficiale 9, versioni precise nel log; Node 22.20.0.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
npm install --prefix .tools @riotjs/compiler@9.4.6 @riotjs/ssr@9; node verify.cjs .tools build
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il vero compiler emette ESM, SSR monta/rende World e Reader con il risultato p esatto. Il goal verificato eÌ€ server rendering; nessun browser richiesto.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://riot.js.org/compiler/](https://riot.js.org/compiler/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.riot` | [corpus-greeting.riot](corpus-greeting.riot) verificato |
