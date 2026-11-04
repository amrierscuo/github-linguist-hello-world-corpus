# 0478: NumPy: `.numsc`

Ruolo: Alias lessicale Python/NumPy: il produttore CAST elenca .numsc tra gli input Python e NumPyLexer eredita PythonLexer. Non si asserisce un formato compilato né compatibilità con loader storici.

Origin: Byte-identical copy of the original corpus source: examples/#478 NumPy/hello.numpy.

Required toolchain: NumPy2.5.3, CPython3.13.9. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Python con NumPy: python hello.numsc. Il parser Python può analizzare i byte letti dal file; non si valida un consumer storico del suffisso.
```

Expected result: Hello, World! and LF; NumPy uint8 array with 13 elements.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.
- The specific historical consumer of .numsc has not been exercised; the proposed verification concerns Python grammar and NumPy operations.

SHA-256 of variant files:

- `hello.numsc`: `48bdd9ee0eeb842f9754fc0f6e1cf7a63d610e67ef01c6cfa3d07f77deb57076`

Primary sources:

- https://doc.castsoftware.com/technologies/multi/com.castsoftware.dmtxmlscanner/1.2/
- https://raw.githubusercontent.com/pygments/pygments/master/pygments/lexers/python.py
- https://numpy.org/doc/stable/reference/generated/numpy.array.html
- https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html
