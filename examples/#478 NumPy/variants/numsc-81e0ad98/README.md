# 0478 — NumPy: `.numsc`

Ruolo: Alias lessicale Python/NumPy: il produttore CAST elenca .numsc tra gli input Python e NumPyLexer eredita PythonLexer. Non si asserisce un formato compilato né compatibilità con loader storici.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#478 NumPy/hello.numpy.

Toolchain richiesta: NumPy2.5.3, CPython3.13.9. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Python con NumPy: python hello.numsc. Il parser Python può analizzare i byte letti dal file; non si valida un consumer storico del suffisso.
```

Risultato atteso: Hello, World! e LF; array NumPy uint8 con 13 elementi.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.
- Il consumer storico specifico di .numsc non è stato esercitato; la verifica proposta riguarda la grammatica Python e le operazioni NumPy.

SHA-256 dei file della variante:

- `hello.numsc`: `48bdd9ee0eeb842f9754fc0f6e1cf7a63d610e67ef01c6cfa3d07f77deb57076`

Fonti primarie:

- https://doc.castsoftware.com/technologies/multi/com.castsoftware.dmtxmlscanner/1.2/
- https://raw.githubusercontent.com/pygments/pygments/master/pygments/lexers/python.py
- https://numpy.org/doc/stable/reference/generated/numpy.array.html
- https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html
