# #706 Tact

Voce e ordine canonici di `reference/languages.yml`.

Compila il sorgente originale e restituisce `Hello, World!` eseguendo il bytecode in una macchina virtuale locale.

## Toolchain e riproduzione

Tact 1.6.13 + TON Sandbox 0.45.0 + tsx 4.23.15; Node.js 22.20.0. Eseguire dalla cartella dell'esempio:

```sh
npm install --no-audit --no-fund --save-exact @tact-lang/compiler@1.6.13 @ton/sandbox@0.45.0 @ton/core@0.63.1 @ton/crypto@3.3.0 tsx@4.23.15
node verify.cjs
```

Il checker compila Tact in una cartella temporanea locale. Usa lo StateInit del wrapper TypeScript prodotto dal compilatore, esegue il getter greeting nella TVM e controlla sia lo stack sia il risultato del wrapper ufficiale. La cartella temporanea viene rimossa al termine.

La verifica usa solo una VM locale e non richiede account, fondi o connessione a una blockchain.

## Stato e prova

Sintassi e semantica verificate il `2026-10-08T23:31:25.959856+00:00`. Risultato reale: `Hello, World!`.

[Log della verifica](verification/runtime.json) con versioni, comandi, stdout, exit code e SHA-256 dei sorgenti e del checker. La prova riguarda questo campione e le versioni indicate.

## Fonti primarie

- [https://docs.tact-lang.org/book/contracts/](https://docs.tact-lang.org/book/contracts/)
- [https://github.com/ton-blockchain/sandbox](https://github.com/ton-blockchain/sandbox)

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.tact` | [hello.tact](hello.tact) sintassi e semantica verificate |
