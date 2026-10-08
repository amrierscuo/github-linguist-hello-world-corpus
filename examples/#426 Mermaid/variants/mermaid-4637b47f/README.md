# 0426 — Mermaid: `.mermaid`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#426 Mermaid/hello.mmd.

Toolchain richiesta: Node.js 22.20.0 + Mermaid 11.12.0 + jsdom 26.1.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.mermaid; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: un nodo greeting con testo Hello, World!; stdout saluto e LF.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.mermaid`: `81d7210bdc34658684885842d1f77c662eddbd92474995475e1df6c91fd7aa5c`
- `verify.cjs`: `aa18c79b58a45b7a4bf1bb3c42aa3ba88deed9ce1a48c4122c60ab2d72591e5f`

Fonti primarie:

- https://mermaid.js.org/syntax/flowchart.html
- https://mermaid.js.org/config/usage.html
