# 0407 — MATLAB: `.matlab`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#407 MATLAB/hello.m.

Toolchain richiesta: MATLAB oppure GNU Octave per questo sottoinsieme compatibile. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.matlab; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: stdout Hello, World! e LF.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.matlab`: `a7c821fc75515533494fb9259e141f9a8206c7aeb15bccdc251747f60d440b60`

Fonti primarie:

- https://www.mathworks.com/help/matlab/ref/disp.html
- https://docs.octave.org/latest/
