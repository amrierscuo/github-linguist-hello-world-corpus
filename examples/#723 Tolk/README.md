# #723 Tolk

Voce e ordine canonici di `reference/languages.yml`.

Compila il sorgente originale e restituisce `Hello, World!` eseguendo il bytecode in una macchina virtuale locale.

## Toolchain e riproduzione

Tolk 1.4.2 + TON Sandbox 0.45.0; Node.js 22.20.0. Eseguire dalla cartella dell'esempio:

```sh
npm install --no-audit --no-fund --save-exact @ton/tolk-js@1.4.2 @ton/sandbox@0.45.0 @ton/core@0.63.1 @ton/crypto@3.3.0
node verify.cjs
```

Il checker compila con Tolk e carica codice e cella dati vuota nel TON Sandbox. Esegue il getter greeting nella TVM e controlla exit code 0 e stringa restituita.

La verifica usa solo una VM locale e non richiede account, fondi o connessione a una blockchain.

## Stato e prova

Sintassi e semantica verificate il `2026-10-08T23:31:23.792787+00:00`. Risultato reale: `Hello, World!`.

[Log della verifica](verification/runtime.json) con versioni, comandi, stdout, exit code e SHA-256 dei sorgenti e del checker. La prova riguarda questo campione e le versioni indicate.

## Fonti primarie

- [https://docs.ton.org/tolk/overview](https://docs.ton.org/tolk/overview)
- [https://github.com/ton-blockchain/tolk-js](https://github.com/ton-blockchain/tolk-js)
- [https://github.com/ton-blockchain/sandbox](https://github.com/ton-blockchain/sandbox)

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.tolk` | [hello.tolk](hello.tolk) sintassi e semantica verificate |
