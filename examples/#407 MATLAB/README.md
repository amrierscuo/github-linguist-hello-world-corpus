# #407 MATLAB

Eseguire uno script MATLAB che stampa Hello, World!.

Tipo canonico `programming`, language_id `225`.

Toolchain prevista: MATLAB oppure GNU Octave per questo sottoinsieme compatibile.

Dalla cartella dell’esempio:

```sh
octave --no-gui --quiet hello.m
```

Risultato atteso: stdout Hello, World! e LF.

Un eventuale test Octave verrà indicato come compatibilità Octave; non si attribuisce una prova al runtime MATLAB senza averlo eseguito.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [MathWorks — disp](https://www.mathworks.com/help/matlab/ref/disp.html)
- [GNU Octave — manuale](https://docs.octave.org/latest/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.matlab` | [hello.matlab](variants/matlab-67b3d23b/hello.matlab) creato, verifiche pendenti |
| `.m` | [hello.m](hello.m) creato, verifiche pendenti |
