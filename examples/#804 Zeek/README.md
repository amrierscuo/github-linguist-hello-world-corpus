# #804 Zeek

Eseguire zeek_init senza cattura di rete.

## Toolchain

Zeek runtime

## Procedura

zeek hello.zeek

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.

Solo avvio dello script locale, nessuna cattura interfaccia o rete.

Requisiti residui:
- Zeek parser/runtime non disponibile.

## Fonti primarie

- [https://docs.zeek.org/en/current/scripting/basics.html](https://docs.zeek.org/en/current/scripting/basics.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.zeek` | [hello.zeek](hello.zeek) creato, verifiche pendenti |
| `.bro` | [hello.bro](variants/bro-c936c4b3/hello.bro) creato, verifiche pendenti |
