# #179 EQ

Definire una classe EQ Greeting con metodo statico value che restituisce Hello, World!.

## Toolchain

EQ del progetto Jkop; toolchain/spec versione non reperita

## Comandi e procedura

Integrare Greeting.eq in un progetto Jkop EQ e chiamare Greeting.value() nel suo harness; comando del compilatore da identificare

## Risultato atteso

Metodo value restituisce esattamente Hello, World!.

## Stato

Sintassi e semantica in attesa.

Identificazione basata sui campioni canonici Linguist: header Jkop/Job and Esther Technologies, public class e metodi public static con return(...). La sintassi somiglia a C#, ma non viene trattata come C# e non si inventa un entrypoint console. Il frammento è originale e la toolchain EQ resta da identificare prima di qualsiasi flag di verifica.

Requisiti residui:
- Compilatore/runtime EQ del progetto Jkop non individuato; nessuna verifica sintattica o chiamata di metodo.

## Fonti primarie e riferimento di formato

- [https://github.com/github-linguist/linguist/blob/main/samples/EQ/String.eq](https://github.com/github-linguist/linguist/blob/main/samples/EQ/String.eq)
- [https://github.com/github-linguist/linguist/blob/main/samples/EQ/SEButtonEntity.eq](https://github.com/github-linguist/linguist/blob/main/samples/EQ/SEButtonEntity.eq)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.eq` | [Greeting.eq](Greeting.eq) creato, verifiche pendenti |
