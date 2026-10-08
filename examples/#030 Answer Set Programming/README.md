# #030 Answer Set Programming

`hello.lp` contiene un fatto di greeting e una direttiva `#show` che mostra soltanto `greeting/1`. Per questo linguaggio dichiarativo il risultato è l'atomo in un answer set, non una stampa imperativa.

Prerequisiti: Python e il pacchetto ufficiale `clingo==5.8.0`. La prova locale ha usato CPython 3.13.9 e wheel Windows x64, installate nella sola cartella di lavoro.

```sh
python -m pip install clingo==5.8.0
python verify.py
```

`verify.py` usa `clingo.Control`, il parser/grounder nativo e il solver. Chiede tutti i modelli, verifica soddisfacibilità ed enumerazione esaustiva e confronta l'intera lista degli atomi mostrati con un solo `greeting("Hello, World!")`. La prima riga stampata dall'helper è `Hello, World!`; la seconda conferma il controllo. La semantica verificata è il risultato del solver, non la sola stampa del helper.

Toolchain: **Potassco clingo 5.8.0 Python wheel; CPython 3.13.9 Windows x64**.

Stato: **Sintassi e semantica verificate.**

Evidenza: [log dei comandi e SHA-256 dei sorgenti](verification/toolchain.json). Il log conserva exit code, stdout e stderr; i percorsi della macchina sono normalizzati.

Fonti primarie:

- [Documentazione / sorgente ufficiale 1](https://potassco.org/clingo/)
- [Documentazione / sorgente ufficiale 2](https://github.com/potassco/clingo/releases/tag/v5.8.0)
- [Documentazione / sorgente ufficiale 3](https://github.com/potassco/clingo/blob/v5.8.0/libpyclingo/clingo/control.py)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.lp` | [hello.lp](hello.lp) verificato |
