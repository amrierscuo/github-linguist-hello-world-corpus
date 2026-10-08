# #801 Yul

Voce e ordine canonici di `reference/languages.yml`.

Compila il sorgente originale e restituisce `Hello, World!` eseguendo il bytecode in una macchina virtuale locale.

## Toolchain e riproduzione

Solc 0.8.37 + EthereumJS EVM 10.1.3; Node.js 22.20.0. Eseguire dalla cartella dell'esempio:

```sh
npm install --no-audit --no-fund --save-exact solc@0.8.37 @ethereumjs/evm@10.1.3
node verify.cjs
```

Il checker esegue i bytecode prodotti da solc con EthereumJS EVM, hardfork Prague. Verifica assenza di eccezioni e tutti i 13 byte restituiti da RETURN.

La verifica usa solo una VM locale e non richiede account, fondi o connessione a una blockchain.

## Stato e prova

Sintassi e semantica verificate il `2026-10-08T23:31:22.707883+00:00`. Risultato reale: `Hello, World!`.

[Log della verifica](verification/runtime.json) con versioni, comandi, stdout, exit code e SHA-256 dei sorgenti e del checker. La prova riguarda questo campione e le versioni indicate.

## Fonti primarie

- [https://docs.soliditylang.org/en/latest/yul.html](https://docs.soliditylang.org/en/latest/yul.html)
- [https://github.com/ethereumjs/ethereumjs-monorepo/tree/master/packages/evm](https://github.com/ethereumjs/ethereumjs-monorepo/tree/master/packages/evm)

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.yul` | [hello.yul](hello.yul) sintassi e semantica verificate |
