# 0418 — Markdown: `.workbook`

Ruolo: Xamarin Workbook testuale con YAML front matter e cella C#.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Python 3.13.9 + markdown-it-py 4.2.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Xamarin Workbooks storico: aprire hello.workbook, selezionare Console e valutare cella
```

Risultato atteso: Hello, World! nella console

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.workbook`: `ae964d6e0f1ce395297aa04bbb4c591d7e1753a103460fcaad5c1344b85553cc`

Fonti primarie:

- https://github.com/microsoft/workbooks
- https://spec.commonmark.org/0.31.2/
- https://github.com/executablebooks/markdown-it-py
