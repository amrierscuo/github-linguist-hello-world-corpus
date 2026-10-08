# #391 Literate Agda

Compilare un programma Agda letterato che usa IO.Main per stampare il saluto.

## Toolchain

Agda e agda-stdlib compatibili; versione da registrare

## Comandi e procedura

agda -i <agda-stdlib/src> --compile Hello.lagda; eseguire il main compilato dalla toolchain Agda/GHC

## Risultato atteso

Blocchi code selezionati; tipo Main accettato; runtime stampa Hello, World!.

## Stato

Sintassi e semantica in attesa.

File LaTeX letterato originale con blocco code; la libreria standard fornisce run/putStrLn e Main. Non basta un compilatore LaTeX per verificare Agda.

Requisiti residui:
- Agda/stdlib/backend GHC non disponibili; type check e IO pending.

## Fonti primarie

- [https://agda.readthedocs.io/en/latest/tools/literate-programming.html](https://agda.readthedocs.io/en/latest/tools/literate-programming.html)
- [https://agda.github.io/agda-stdlib/v2.0/IO.html](https://agda.github.io/agda-stdlib/v2.0/IO.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.lagda` | [Hello.lagda](Hello.lagda) creato, verifiche pendenti |
