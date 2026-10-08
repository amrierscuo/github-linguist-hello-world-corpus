# #199 F*

Controllare i tipi di una funzione F* con effetto ML che stampa Hello, World!, poi estrarla ed eseguirla.

Tipo canonico `programming`, language_id `336943375`.

Toolchain prevista: F* e backend OCaml con libreria FStar.IO e Z3 compatibile.

Dalla cartella dell’esempio:

```sh
fstar.exe Hello.fst
```

Risultato atteso: modulo accettato dal typechecker; chiamando main del modulo estratto, stdout `Hello, World!\n`.

Il comando documentato verifica i tipi, ma non esegue main. Estrazione OCaml, linking del runtime e chiamata a main restano una prova separata; non sono sostituiti da una semplice ricerca della stringa nel file.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain nativa non ancora eseguita: le verifiche di sintassi e semantica restano pendenti.

Fonti del linguaggio/formato e implementazioni originali:

- [F* — guida alla toolchain](https://fstar-lang.org/tutorial/book/part1/part1_getting_off_the_ground.html)
- [FStar.IO — interfaccia originale](https://github.com/FStarLang/FStar/blob/master/ulib/FStar.IO.fsti)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.fst` | [Hello.fst](Hello.fst), [Hello.fst](variants/ext-fsti-2e66737469/Hello.fst) creato, verifiche pendenti |
| `.fsti` | [Hello.fsti](variants/ext-fsti-2e66737469/Hello.fsti) creato, verifiche pendenti |
