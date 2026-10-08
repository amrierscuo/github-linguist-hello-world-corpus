# #390 Liquidsoap

Valutare uno script Liquidsoap che stampa il saluto senza configurare streaming.

## Toolchain

Liquidsoap; versione da registrare

## Comandi e procedura

liquidsoap --check hello.liq; liquidsoap --check-and-evaluate hello.liq (verificare disponibilità opzione nella versione scelta)

## Risultato atteso

Tipo del print accettato; valutazione scrive Hello, World!.

## Stato

Sintassi e semantica in attesa.

Il campione è puro testo e non apre sorgenti, device o stream. Il comando di valutazione deve essere adattato/registrato secondo il CLI effettivo; non si conta un parser generico OCaml.

Requisiti residui:
- Runtime Liquidsoap non predisposto; parsing/type check e valutazione pending.

## Fonti primarie

- [https://www.liquidsoap.info/doc-2.2.5/language.html](https://www.liquidsoap.info/doc-2.2.5/language.html)
- [https://www.liquidsoap.info/doc-2.2.5/script_loading.html](https://www.liquidsoap.info/doc-2.2.5/script_loading.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.liq` | [hello.liq](hello.liq) creato, verifiche pendenti |
