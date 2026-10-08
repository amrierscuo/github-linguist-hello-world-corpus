# #803 ZIL

Compilare il sorgente originale ZIL e assemblare/eseguire il saluto Z-machine.

## Toolchain

ZILF 1.9; ZAPF 1.9; Frotz2.54

## Procedura

zilf build hello.zil build/hello.zap -S; zapf build/hello.zap; dfrotz -m build/hello.z3

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

La voce ZAP contiene assembly testuale generato realmente dal nostro sorgente ZIL originale, più i file include del compiler. Il binario Z-machine resta in work.

Verifica reale 2026-10-08T13:38:32.256505+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://github.com/taradinoc/zilf](https://github.com/taradinoc/zilf)
- [https://github.com/taradinoc/zilf/releases/tag/1.9](https://github.com/taradinoc/zilf/releases/tag/1.9)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.zil` | [hello.zil](hello.zil) verificato |
| `.mud` | [hello.mud](variants/mud-6f2646fc/hello.mud) creato, verifiche pendenti |
