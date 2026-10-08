# #397 Logos

Espandere %ctor Logos e definire un costruttore Objective-C che usa NSLog.

## Toolchain

Theos Logos master snapshot; This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi

## Comandi e procedura

perl logos.pl -c generator=internal -c warnings=error hello.xm; compilare il risultato Objective-C nel target Apple di prova e avviare il costruttore

## Risultato atteso

Preprocessore senza errori genera constructor; NSLog del target contiene Hello, World!.

## Stato

Sintassi verificata; semantica in attesa.

Il preprocessore Perl originale espande la direttiva e conserva NSLog; sono registrati hash di tutti i file del tool snapshot. Questa prova valida soltanto la sintassi Logos/preprocessing. Foundation e runtime Apple non sono stati simulati né eseguiti.

Verifica effettiva del 2026-10-08T12:48:20.545080+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

Requisiti residui:
- Apple Foundation Objective-C compile/runtime unavailable; NSLog execution pending.

## Fonti primarie

- [https://theos.dev/docs/logos](https://theos.dev/docs/logos)
- [https://theos.dev/docs/logos-syntax](https://theos.dev/docs/logos-syntax)
- [https://github.com/theos/logos](https://github.com/theos/logos)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.xm` | [hello.xm](hello.xm) sintassi verificata |
| `.x` | [hello.x](variants/x-bb42e4c6/hello.x) creato, verifiche pendenti |
| `.xi` | [hello.xi](variants/xi-347cda4a/hello.xi) creato, verifiche pendenti |
