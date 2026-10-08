# #013 API Blueprint

`hello.apib` descrive una risorsa `GET /hello` con risposta HTTP 200, tipo
`text/plain` e corpo `Hello, World!` seguito da un ritorno a capo. È un documento
di contratto API; non avvia un server HTTP.

## Toolchain e comando

Serve Node.js e il parser ufficiale Drafter.js 3.2.0, la versione JavaScript
compilata dal parser C++ di API Blueprint. È possibile installarlo localmente:

```powershell
npm install --prefix .tools --ignore-scripts --no-audit --no-fund drafter.js@3.2.0
node verify.cjs .tools/node_modules/drafter.js
```

`verify.cjs` chiede prima a Drafter di validare il documento senza diagnostiche,
poi verifica nel suo AST metodo, percorso, stato, tipo e corpo della risposta.
Non implementa un parser del formato.

## Verifica eseguita

Sintassi e semantica del **contratto documentale** verificate su Windows con
Drafter.js 3.2.0. Risultato atteso e osservato:

```text
Drafter: valid, no warnings
AST: GET /hello -> 200 text/plain; body = Hello, World! + LF
```

Il controllo non prova il comportamento di un server: questo esempio non ne
contiene uno. I file del parser sono in una cartella di lavoro esterna al corpus;
origine, SHA-256 e comando eseguito sono registrati in `verification.log`.

## Fonti primarie

- [API Blueprint: specifica](https://apiblueprint.org/documentation/specification.html)
- [API Blueprint: strumenti di parsing](https://apiblueprint.org/developers.html)
- [Repository ufficiale Drafter.js e API parseSync/validateSync](https://github.com/apiaryio/drafter.js)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.apib` | [hello.apib](hello.apib) verificato |
