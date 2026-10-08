# #192 Elvish

Eseguire uno script Elvish e stampare Hello, World! seguito da LF.

Tipo canonico `programming`, language_id `570996448`.

Toolchain prevista: Elvish 0.21.0.

Dalla cartella dell’esempio:

```sh
elvish hello.elv
```

Risultato atteso: stdout esatto `Hello, World!\n`, uscita 0.

echo è una funzione builtin Elvish. La stringa è quotata e non espande variabili o comandi.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Elvish 0.21.0 windows/amd64. Vedere [log](verification/verification.log). 

Fonti del linguaggio/formato e implementazioni originali:

- [Elvish — tour](https://elv.sh/learn/tour.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.elv` | [hello.elv](hello.elv) verificato |
