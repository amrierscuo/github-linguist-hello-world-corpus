# #081 Bru

Inviare una richiesta GET locale a hello.txt con Bruno e verificare nel test della richiesta che la risposta contenga Hello, World!.

## Toolchain

Node.js v22.20.0; @usebruno/lang 0.40.0; @usebruno/cli 4.2.1; Python stdlib HTTP fixture 3.13.9

## Comandi e procedura

I comandi vanno eseguiti dalla cartella dell'esempio. `npm install` installa
localmente parser e CLI alle versioni fissate in package.json. `node check.cjs`
attesta il formato del file Bru. Avviare la fixture in un terminale:

```sh
python -m http.server 8765 --bind 127.0.0.1
```

Poi, da un altro terminale nella medesima cartella:

```sh
npx bru run hello.bru --noproxy --sandbox=safe
```

Terminare il server quando la prova finisce. La verifica registrata ha avviato
e chiuso automaticamente una fixture equivalente, ed eseguito una richiesta
e il test Bruno reale. Non sono necessari credenziali o endpoint esterni.

## Risultato atteso

Una richiesta GET, HTTP 200; corpo Hello, World! seguito da newline; test response greeting passa; exit 0.

## Stato

Sintassi e semantica verificate.

Il server è una fixture temporanea su loopback che serve hello.txt. Il parser e il runner sono quelli ufficiali Bruno. Il comando node check.cjs controlla il formato; il comando bru esegue anche HTTP e test.

Verifica effettiva del 2026-10-08T11:38:40.631298+00:00 su Windows x64: [log](verification/result.json).
Il log include hash SHA-256 della sorgente e dei checker, versioni, comandi, codici di uscita, stdout, stderr e limiti della prova.

## Fonti primarie

- [https://docs.usebruno.com/bru-lang/overview](https://docs.usebruno.com/bru-lang/overview)
- [https://docs.usebruno.com/bru-cli/run/options](https://docs.usebruno.com/bru-cli/run/options)
- [https://github.com/usebruno/bruno](https://github.com/usebruno/bruno)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bru` | [hello.bru](hello.bru) verificato |
