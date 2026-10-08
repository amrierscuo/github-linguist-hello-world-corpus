# #486 OMNeT++ MSG

Generare il messaggio e avviare una rete OMNeT++ che registra il saluto.

## Toolchain

OMNeT++ 6.2 compatibile

## Procedura

opp_makemake -f --deep -o hello; make; ./hello -u Cmdenv -f omnetpp.ini

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.

Il pacchetto include MSG/NED, modulo C++ e configurazione originali; il goal usa il campo generato del messaggio.

Requisiti residui:
- opp_msgtool, compilatore NED e librerie/runtime OMNeT++ non predisposti.

## Fonti primarie

- [https://doc.omnetpp.org/omnetpp/manual/](https://doc.omnetpp.org/omnetpp/manual/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.msg` | [Greeting.msg](Greeting.msg) creato, verifiche pendenti |
