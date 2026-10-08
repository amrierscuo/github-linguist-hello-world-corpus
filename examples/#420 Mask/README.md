# #420 Mask

Analizzare Mask e renderizzare una interpolazione del modello target.

Tipo canonico `markup`, language_id `223`.

Toolchain prevista: Node.js 22 e MaskJS originale.

Dalla cartella dell’esempio:

```sh
node verify.cjs
```

Risultato atteso: HTML <p>Hello, World!</p>; stdout saluto e LF.

La stringa è interpolata dal motore MaskJS; non viene sostituita da un helper che imita il formato.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Node.js 22.20.0 + MaskJS 0.73.3. [Log](verification/result.json). 

Fonti:

- [MaskJS — motore originale](https://github.com/atmajs/MaskJS)

Dipendenza fissata: `npm install --ignore-scripts --no-audit --no-fund maskjs@0.73.3`. La build Node espone render, usato dal checker.

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mask` | [hello.mask](hello.mask) verificato |
