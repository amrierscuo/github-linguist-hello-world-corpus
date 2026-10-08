# #146 Curry

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Eseguire l’azione IO main di Curry e stampare Hello, World!.

Hello.curry dichiara un modulo e l’azione main :: IO (). ++ concatena le stringhe, putStrLn effettua l’IO. La verifica richiede un compilatore Curry autentico, con runtime Prolog/Haskell previsto dalla sua implementazione.

## Toolchain e riproduzione

PAKCS o altra implementazione Curry; versione effettiva da registrare

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
Nella REPL PAKCS: :load Hello
Poi valutare: main
Infine: :quit
```

## Risultato atteso e stato

stdout Hello, World! seguito da newline.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Il sorgente è documentato; parser/compilatore/runtime nativo non è stato eseguito per questa voce.

Impedimenti: PAKCS/KiCS2 e il relativo runtime non disponibili; nessun parser Curry è stato eseguito.

## Fonti primarie

- https://www.curry-language.org/docs/tutorial/html/curry-tutorial.Ch3.S15.html
- https://www.curry-lang.org/pakcs/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.curry` | [Hello.curry](Hello.curry) creato, verifiche pendenti |
