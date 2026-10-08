# 0433 — MiniYAML: `.yml`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#433 MiniYAML/hello.yaml.

Toolchain richiesta: OpenRA MiniYaml parser originale. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.yml; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: un nodo Greeting, figlio Text uguale a Hello, World!.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.yml`: `a02b7e15969b17e696b80411283911ddc48042f60463ac8024881b8df9d586aa`

Fonti primarie:

- https://www.openra.net/book/modding/miniyaml/index.html
- https://github.com/OpenRA/OpenRA/blob/bleed/OpenRA.Game/MiniYaml.cs
