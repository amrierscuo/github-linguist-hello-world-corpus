# 0478 — NumPy: `.numpyw`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#478 NumPy/hello.numpy.

Toolchain richiesta: NumPy2.5.3, CPython3.13.9. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.numpyw; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Hello, World! seguito da newline; exit0.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.numpyw`: `48bdd9ee0eeb842f9754fc0f6e1cf7a63d610e67ef01c6cfa3d07f77deb57076`

Fonti primarie:

- https://numpy.org/doc/stable/reference/generated/numpy.array.html
- https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html
