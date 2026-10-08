# #170 Dotenv

Leggere GREETING dal formato Dotenv e popolarlo in un oggetto isolato.

## Toolchain

Node.js v22.20.0; dotenv 18.0.6

## Comandi e procedura

npm install; node check.cjs

## Risultato atteso

Oggetto esattamente {GREETING:"Hello, World!"}; saluto stampato e exit 0.

## Stato

Sintassi e semantica verificate.

Il file .env.example contiene solo un saluto illustrativo, senza credenziali. dotenv.parse interpreta le virgolette; populate usa un oggetto separato e non cambia l’ambiente della macchina.

Verifica effettiva del 2026-10-08T11:56:13.144812+00:00 su Windows x64: [log](verification/result.json).
Hash delle sorgenti/checker, versioni e comandi reali, codici di uscita, stdout/stderr e limiti della prova sono nel log.

## Fonti primarie e riferimento di formato

- [https://github.com/motdotla/dotenv#usage](https://github.com/motdotla/dotenv#usage)
- [https://github.com/motdotla/dotenv#parse](https://github.com/motdotla/dotenv#parse)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.env` | [hello.env](variants/ext-env-2e656e76/hello.env) creato, verifiche pendenti |
