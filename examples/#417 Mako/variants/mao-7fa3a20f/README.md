# 0417 — Mako: `.mao`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#417 Mako/hello.mako.

Toolchain richiesta: Python 3.13.9 + Mako 1.4.3. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.mao; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: stdout Hello, World! e LF, exit 0.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.mao`: `add1ff9a5370e224b33c18df89e709f00ed56d5c1cac0e0a895f9e85555b63d0`
- `verify.py`: `816bad55b8f7d799691457565d7fe3e4559528a2b1f3464f273de81eadfc3879`

Fonti primarie:

- https://docs.makotemplates.org/en/latest/syntax.html
