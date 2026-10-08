# #382 Lex

Generare un lexer Lex che riconosce hello e stampa Hello, World!.

## Toolchain

flex 2.6.4; GCC 13.3.0

## Comandi e procedura

flex -o build/hello.c hello.l; gcc build/hello.c -o build/hello; build/hello < input.txt

## Risultato atteso

Scanner exit 0; una riga Hello, World!.

## Stato

Sintassi e semantica verificate.

Regex e azioni sono interpretate da Flex originale, il C generato viene compilato ed eseguito. Spazi/newline vengono ignorati; caratteri inattesi producono errore. input.txt rende riproducibile la scansione.

Verifica effettiva del 2026-10-08T12:48:20.760493+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://westes.github.io/flex/manual/](https://westes.github.io/flex/manual/)
- [https://westes.github.io/flex/manual/Simple-Examples.html](https://westes.github.io/flex/manual/Simple-Examples.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.l` | [hello.l](hello.l) verificato |
| `.lex` | [hello.lex](variants/lex-9335749c/hello.lex) creato, verifiche pendenti |
