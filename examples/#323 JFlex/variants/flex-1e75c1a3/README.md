# 0323 — JFlex: `.flex`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#323 JFlex/hello.jflex.

Toolchain richiesta: JFlex 1.9.1 + CUP runtime 11b-20160615-3 + OpenJDK 21.0.12. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.flex; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: uscita 0; stdout Hello, World! seguito da newline.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.flex`: `7038d4ba02a30781506a19f385ae8b2ea69fc9aa5183d8e50fc681dee81a0edf`
- `input.txt`: `aa1db5c660d3d1f3f4f9361b9848694300929be94b74c84452a87420c59e5df9`

Fonti primarie:

- https://jflex.de/manual.html
