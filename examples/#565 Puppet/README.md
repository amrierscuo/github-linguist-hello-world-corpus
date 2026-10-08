# #565 Puppet

Applicare una risorsa notify Puppet.

## Toolchain

Puppet

## Procedura

puppet parser validate hello.pp; puppet apply hello.pp

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.



Requisiti residui:
- Puppet parser/catalog/runtime Ruby non predisposti.

## Fonti primarie

- [https://www.puppet.com/docs/puppet/8/types/notify.html](https://www.puppet.com/docs/puppet/8/types/notify.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pp` | [hello.pp](hello.pp) creato, verifiche pendenti |
