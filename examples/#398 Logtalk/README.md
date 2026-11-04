# #398 Logtalk

Send the message to a Logtalk object and print the greeting.

## Toolchain

Logtalk 3.102.0 original lgt31020stable; SWI-Prolog version 9.0.4 for x86_64-linux

## Commands and procedure

Configurare LOGTALKHOME/LOGTALKUSER locali e SWI_HOME_DIR; swipl -q -f <logtalk>/integration/logtalk_swi.pl -g "logtalk_load(hello,[report(off)]),hello::greet,halt"

## Expected result

Oggetto/public preached compiled; message send emette Hello, World! more newline, exit 0.

## Status

syntax and behavior verified.

Il compilatore Logtalk autentico genera codice per SWI e il backend Prolog lo esegue realmente. Configurazione utente/librerie/cache restano in work.

Actual verification of 2026-10-08T12:51:45.286956+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://logtalk.org/learning.html](https://logtalk.org/learning.html)
- [https://logtalk.org/documentation.html](https://logtalk.org/documentation.html)
- [https://github.com/LogtalkDotOrg/logtalk3/tree/lgt31020stable](https://github.com/LogtalkDotOrg/logtalk3/tree/lgt31020stable)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.lgt` | [hello.lgt](hello.lgt) verified |
| `.logtalk` | [hello.logtalk](variants/logtalk-5d6091a5/hello.logtalk) created; verification pending |
