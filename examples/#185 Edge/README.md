# #185 Edge

Renderizzare un template Edge sostituendo target con World e ottenere Hello, World!.

Tipo canonico `markup`, language_id `460509620`.

Toolchain prevista: Node.js 22 e edge.js 6.5.1.

Dalla cartella dell’esempio:

```sh
node verify.cjs
```

Risultato atteso: stdout esatto `Hello, World!\n`, uscita 0.

Il dato passato al renderer è locale e costante. Non viene avviato un server web.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Node.js 22.20.0 + edge.js 6.5.1. Vedere [log](verification/verification.log). 

Fonti del linguaggio/formato e implementazioni originali:

- [Edge — documentazione del motore](https://edgejs.dev/docs/introduction)
- [Edge — implementazione](https://github.com/edge-js/edge)

Preparazione delle dipendenze in una cartella dedicata:

```sh
npm install --ignore-scripts --no-audit --no-fund edge.js@6.5.1
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.edge` | [hello.edge](hello.edge) verificato |
