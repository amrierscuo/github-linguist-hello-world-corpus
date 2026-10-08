# #647 Salt

Valutare uno stato Salt che mostra una notifica locale.

## Toolchain

Salt local state runtime

## Procedura

salt-call --local --file-root=<cartella> state.apply hello

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.



Requisiti residui:
- Salt renderer/state runtime non disponibile; YAML generico non prova lo stato.

## Fonti primarie

- [https://docs.saltproject.io/en/latest/ref/states/all/salt.states.test.html](https://docs.saltproject.io/en/latest/ref/states/all/salt.states.test.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sls` | [hello.sls](hello.sls) creato, verifiche pendenti |
