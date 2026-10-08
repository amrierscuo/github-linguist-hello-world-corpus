# #101 CWeb

Estrarre un programma C dal sorgente CWEB, compilarlo e stampare Hello, World! seguito da LF.

Tipo canonico: `programming`; `language_id`: `657332628`.

Toolchain prevista: CWEB 4.x (ctangle) e compilatore C conforme a C11. La versione effettivamente provata, quando disponibile, è nel log.

Dalla cartella dell'esempio, con le dipendenze nel PATH:

```sh
ctangle hello.w
cc -std=c11 -Wall -Wextra hello.c -o hello
./hello
```

Risultato atteso: stdout esatto `Hello, World!\n`, uscita 0.

Il controllo di ctangle riguarda il sorgente .w; la compilazione C controlla il codice estratto. La composizione tipografica con cweave/TeX è un passaggio distinto.

Stato registrato: sintassi verificata; semantica verificata. Toolchain provata: MiKTeX CTANGLE (version banner in log) + GCC 13.3.0 on WSL Ubuntu 24.04. Vedere [log](verification/verification.log). 

Fonti primarie o riferimenti originali del progetto:

- [CWEB — Knuth e Levy](https://www-cs-faculty.stanford.edu/~knuth/cweb.html)
- [Implementazione CWEB](https://github.com/ascherer/cweb)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.w` | [hello.w](hello.w) verificato |
