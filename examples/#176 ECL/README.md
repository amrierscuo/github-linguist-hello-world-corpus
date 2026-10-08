# #176 ECL

Restituire una stringa scalare Hello, World! come risultato OUTPUT di un workunit HPCC ECL.

## Toolchain

HPCC Systems ECL compiler eclcc e cluster locale; versioni da registrare

## Comandi e procedura

eclcc -syntax hello.ecl; eseguire hello.ecl nella IDE/Playground del cluster di sviluppo locale e leggere Results

## Risultato atteso

Sintassi accettata; risultato scalare del workunit contiene Hello, World!.

## Stato

Sintassi e semantica in attesa.

ECL qui significa Enterprise Control Language di HPCC Systems. OUTPUT restituisce un risultato del workunit; non si dichiara uno stdout console. La voce distinta ECLiPSe usa invece Prolog.

Requisiti residui:
- eclcc e cluster HPCC locale non disponibili; parsing e risultato workunit pending.

## Fonti primarie e riferimento di formato

- [https://hpccsystems.com/wp-content/uploads/_documents/ECLR_EN_US/OUTPUT.html](https://hpccsystems.com/wp-content/uploads/_documents/ECLR_EN_US/OUTPUT.html)
- [https://hpccsystems.com/training/documentation/learning-ecl/](https://hpccsystems.com/training/documentation/learning-ecl/)
- [https://github.com/hpcc-systems/HPCC-Platform/blob/master/ecl/eclcc/eclcc.hpp](https://github.com/hpcc-systems/HPCC-Platform/blob/master/ecl/eclcc/eclcc.hpp)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ecl` | [hello.ecl](hello.ecl) creato, verifiche pendenti |
| `.eclxml` | [hello.eclxml](variants/ext-eclxml-2e65636c786d6c/hello.eclxml) creato, verifiche pendenti |
