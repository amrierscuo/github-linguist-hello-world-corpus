# #801 Yul

Compilare Yul che restituisce 13 byte del saluto dal buffer EVM.

## Toolchain

Solc 0.8.37+commit.f401782d.Emscripten.clang; Node22.20.0

## Procedura

npm install solc; node verify.cjs build/compiled.json; eseguire il bytecode in una EVM offline e decodificare i byte restituiti.

## Risultato atteso

Hello, World!

## Stato

Sintassi verificata; semantica in attesa.

Nessun deployment; mstore usa il literal left-aligned documentato e return seleziona i 13 byte.

Verifica reale 2026-10-08T13:38:33.424893+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

Requisiti residui:
- Offline EVM execution pending.

## Fonti primarie

- [https://docs.soliditylang.org/en/latest/yul.html](https://docs.soliditylang.org/en/latest/yul.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.yul` | [hello.yul](hello.yul) sintassi verificata |
