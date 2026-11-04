# #302 IGOR Pro

Run HelloWorld in Igor Pro and write greeting in History.

## Toolchain

WaveMetrics Igor Pro; versione da registrare

## Commands and procedure

Upload hello.ipf in the Procedures window; Complete; in the Igor command: HelloWorld()

## Expected result

History contains Hello, World!.

## Status

Syntax and behavioral verification pending.

La funzione originale usa Print; rtGlobals=3 sceglie l’accesso moderno rigoroso alle variabili. Nessuna finestra/grafico è necessaria per il risultato.

Remaining requirements:
- Igor Pro proprietario/licenza unavailable; compilazione e History pending.

## Primary sources

- [https://www.wavemetrics.com/products/igorpro/programming](https://www.wavemetrics.com/products/igorpro/programming)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ipf` | [hello.ipf](hello.ipf) created; verification pending |
