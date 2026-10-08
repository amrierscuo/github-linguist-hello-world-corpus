# #398 Logtalk

Inviare il messaggio greet a un oggetto Logtalk e stampare il saluto.

## Toolchain

Logtalk 3.102.0 original lgt31020stable; SWI-Prolog version 9.0.4 for x86_64-linux

## Comandi e procedura

Configurare LOGTALKHOME/LOGTALKUSER locali e SWI_HOME_DIR; swipl -q -f <logtalk>/integration/logtalk_swi.pl -g "logtalk_load(hello,[report(off)]),hello::greet,halt"

## Risultato atteso

Oggetto/public predicate compilati; message send emette Hello, World! più newline, exit 0.

## Stato

Sintassi e semantica verificate.

Il compilatore Logtalk autentico genera codice per SWI e il backend Prolog lo esegue realmente. Configurazione utente/librerie/cache restano in work.

Verifica effettiva del 2026-10-08T12:51:45.286956+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://logtalk.org/learning.html](https://logtalk.org/learning.html)
- [https://logtalk.org/documentation.html](https://logtalk.org/documentation.html)
- [https://github.com/LogtalkDotOrg/logtalk3/tree/lgt31020stable](https://github.com/LogtalkDotOrg/logtalk3/tree/lgt31020stable)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.lgt` | [hello.lgt](hello.lgt) verificato |
| `.logtalk` | [hello.logtalk](variants/logtalk-5d6091a5/hello.logtalk) creato, verifiche pendenti |
