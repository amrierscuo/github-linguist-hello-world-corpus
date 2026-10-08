# #213 Fluent

Voce canonica `Fluent`, tipo `programming`, language_id `206353404`.

Analizzare il messaggio di localizzazione Fluent e renderizzare Hello, World! con una variabile name; controllare anche Reader.

## Toolchain e riproduzione

Official Mozilla Fluent syntax AST and runtime bundle — @fluent/syntax 0.19.0; @fluent/bundle 0.19.1; v22.20.0. Ambiente della prova: **Windows x64**.

Node.js 22.20.0 e pacchetti ufficiali Mozilla Fluent fissati alle versioni indicate. .tools va collocata in una copia di lavoro.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
npm install --prefix .tools @fluent/syntax@0.19.0 @fluent/bundle@0.19.1; node verify.cjs .tools hello.ftl
```

Risultato atteso: Saluto World e controllo Reader corretti; PASS.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il parser ufficiale deve produrre zero Junk; FluentBundle riceve una FluentResource e controlla errori e rendering parametrico. useIsolating=false rende il confronto testuale esplicito. Questa .ftl è localizzazione Fluent.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sorgenti verificati in staging. I soli probe di disponibilità non attestano parsing
o esecuzione. Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://projectfluent.org/](https://projectfluent.org/)
- [https://github.com/projectfluent/fluent.js](https://github.com/projectfluent/fluent.js)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ftl` | [hello.ftl](hello.ftl) verificato |
