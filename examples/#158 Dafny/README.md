# #158 Dafny

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Dimostrare stringa e lunghezza del saluto in Dafny, compilare in JavaScript ed eseguirlo.

Le assert dimostrano valore e lunghezza 13. La prova SMT precede la compilazione/esecuzione del backend JavaScript. Il log distingue esito del verificatore e output runtime; il backend usa bignumber.js isolato tramite NODE_PATH. Il runner effettivo carica DafnyDriver.dll con dotnet.

## Toolchain e riproduzione

Dafny 3.13.1.50302; .NET 6.0.36; Z3 5.1.0; Node.js 22.20.0; bignumber.js

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
dafny /compile:0 /proverOpt:PROVER_PATH=<z3> hello.dfy
```

```text
dafny /compileTarget:js /compile:3 /proverOpt:PROVER_PATH=<z3> hello.dfy
```

## Risultato atteso e stato

1 verified, 0 errors; il programma compilato emette Hello, World! e newline.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra versioni e provenienza, SHA-256 dei sorgenti, comandi effettivi, exit, stdout e stderr normalizzati.

## Fonti primarie

- https://dafny.org/dafny/DafnyRef/DafnyRef
- https://github.com/dafny-lang/dafny

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.dfy` | [hello.dfy](hello.dfy) verificato |
