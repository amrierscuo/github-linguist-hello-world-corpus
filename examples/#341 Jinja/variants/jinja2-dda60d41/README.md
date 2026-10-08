# 0341 — Jinja: `.jinja2`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#341 Jinja/hello.jinja.

Toolchain richiesta: Official Jinja compiler/runtime — jinja2 3.1.6. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.jinja2; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Hello, World! e PASS dei controlli parametrici.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.jinja2`: `193487ca91af7ec5fdfd1d0850dfae6f0bbe25258cc0378905c24e65099f8cfb`
- `verify.py`: `e65c4372f6fcde0a04087628c1c84fc91a740aa4a7beadce3906f994e8727d5d`

Fonti primarie:

- https://jinja.palletsprojects.com/en/stable/api/
- https://jinja.palletsprojects.com/en/stable/templates/
