# #118 Cirru

Compilare un’espressione CirruScript dalla grammatica Cirru in JavaScript ed eseguirla per stampare Hello, World!.

Tipo canonico: `programming`; `language_id`: `58`.

Toolchain prevista: Node.js 22 e cirru-script 0.6.2 (implementazione originale storica). La versione effettivamente provata, quando disponibile, è nel log.

Dalla cartella dell'esempio, con le dipendenze nel PATH:

```sh
cirruscript hello.cirru
```

Risultato atteso: stdout `Hello, World!` seguito da newline.

Cirru è una grammatica utilizzabile da più linguaggi; questo esempio seleziona esplicitamente il dialetto CirruScript storico. Il parser della grammatica da solo non prova l’esecuzione del saluto.

Stato registrato: sintassi verificata; semantica verificata. Toolchain provata: Node.js 22.20.0 + cirru-script 0.6.2. Vedere [log](verification/verification.log). 

Fonti primarie o riferimenti originali del progetto:

- [CirruScript — compilatore originale](https://github.com/Cirru/cirru-script)
- [Cirru — parser originale](https://github.com/Cirru/parser.coffee)

Verifica automatica inclusa: `node verify.cjs`.

Dipendenze riproducibili in una cartella di lavoro dedicata:

```sh
npm install --ignore-scripts --no-audit --no-fund cirru-script@0.6.2
```

In CirruScript il prefisso `:` identifica un valore stringa. Le virgolette proteggono gli spazi del token; il prefisso non fa parte del testo stampato.

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cirru` | [hello.cirru](hello.cirru) verificato |
