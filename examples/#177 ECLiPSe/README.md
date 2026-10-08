# #177 ECLiPSe

Caricare un predicato main in ECLiPSe Prolog ed eseguire printf del saluto.

## Toolchain

Official ECLiPSe CLP 7.2

## Comandi e procedura

eclipse -e "get_flag(version, V), writeln(V)"; eclipse -b hello.ecl -e main

## Risultato atteso

Caricamento exit 0; main scrive Hello, World! più newline, exit 0.

## Stato

Sintassi e semantica verificate.

Runtime nativo ufficiale ECLiPSe CLP. La distribuzione portabile usa ECLIPSEDIR per trovare il proprio kernel e le librerie. %n è il controllo formato della newline; niente dipendenza da HPCC.

Verifica effettiva del 2026-10-08T12:01:23.327370+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Hash delle sorgenti/checker, versioni e comandi reali, codici di uscita, stdout/stderr e limiti della prova sono nel log.

## Fonti primarie e riferimento di formato

- [https://eclipseclp.org/](https://eclipseclp.org/)
- [https://www.eclipseclp.org/doc/bips/kernel/ioterm/printf-2.html](https://www.eclipseclp.org/doc/bips/kernel/ioterm/printf-2.html)
- [https://eclipseclp.org/Distribution/Builds/7.2_13/x86_64_linux/](https://eclipseclp.org/Distribution/Builds/7.2_13/x86_64_linux/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ecl` | [hello.ecl](hello.ecl) verificato |
