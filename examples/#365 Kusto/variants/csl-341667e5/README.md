# 0365 — Kusto: `.csl`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#365 Kusto/hello.kql.

Toolchain richiesta: Microsoft.Azure.Kusto.Language12.4.1; PowerShell7 per il driver; query engine non preparato. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.csl; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Parser e analizzatore producono zero diagnostiche; engine atteso: una riga greeting=Hello, World!.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.csl`: `70a3f13183759f7b0b96a2d2ef87da52e07baa0cfadc89a08880c41a92a66b01`
- `verify.ps1`: `2541d629bb8ade880fe6eab58368c231f742a024c7f4fa55df1d26b0503f4a31`

Fonti primarie:

- https://learn.microsoft.com/en-us/kusto/query/print-operator
- https://learn.microsoft.com/en-us/kusto/query/strcat-function
- https://github.com/microsoft/Kusto-Query-Language
