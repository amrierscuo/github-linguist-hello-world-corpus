# 0398 — Logtalk: `.logtalk`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#398 Logtalk/hello.lgt.

Toolchain richiesta: Logtalk 3.102.0 original lgt31020stable; SWI-Prolog version 9.0.4 for x86_64-linux. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.logtalk; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Oggetto/public predicate compilati; message send emette Hello, World! più newline, exit 0.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.logtalk`: `c773f66269f7f241a6271a1c3574ace6668fb76844ecaa0996ad38cb010578ad`

Fonti primarie:

- https://logtalk.org/learning.html
- https://logtalk.org/documentation.html
- https://github.com/LogtalkDotOrg/logtalk3/tree/lgt31020stable
