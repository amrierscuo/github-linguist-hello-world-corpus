# 0502 — OpenCL: `.opencl`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#502 OpenCL/hello.cl.

Toolchain richiesta: Clang18.1.3 originale per OpenCL C1.2; runtime/device non predisposto. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.opencl; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: kernel valido; dispatch di 13 elementi produce Hello, World!.

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Parser del linguaggio accettato; schema/loader/semantica applicativa specifici restano non verificati.

SHA-256 dei file della variante:

- `hello.opencl`: `e0819012bd9433a1443054f2d398e8f78cbb078fb35a76d0dc49dbcf205b0a9e`

Fonti primarie:

- https://registry.khronos.org/OpenCL/specs/3.0-unified/html/OpenCL_C.html

Prova aggiuntiva realmente eseguita:

Clang originale -x cl -cl-std=CL1.2 -fsyntax-only sul file .opencl. Nessuna GPU/device o esecuzione del kernel.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: 18.1.3
