# #498 Opal

Mostrare il saluto con alert nel dialetto .opal della baseline.

## Toolchain

Runtime Opal compatibile con StoneCypher/DeepakChopra_Opal

## Procedura

Caricare hello.opal nel runtime compatibile con il campione upstream; registrare compiler e procedura effettivi.

## Risultato atteso

Finestra alert con Hello, World!.

## Stato

Sintassi e semantica in attesa.

La scelta di alert e commenti -- segue il campione Linguist/upstream; non viene sostituita con il linguaggio Ruby Opal o con il distinto OPAL algebrico.

Requisiti residui:
- Il runtime/compilatore storico del dialetto .opal non è stato identificato e predisposto.

## Fonti primarie

- [https://github.com/StoneCypher/DeepakChopra_Opal](https://github.com/StoneCypher/DeepakChopra_Opal)
- [https://github.com/github-linguist/linguist/blob/main/samples/Opal/DeepakChopra.opal](https://github.com/github-linguist/linguist/blob/main/samples/Opal/DeepakChopra.opal)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.opal` | [hello.opal](hello.opal) creato, verifiche pendenti |
