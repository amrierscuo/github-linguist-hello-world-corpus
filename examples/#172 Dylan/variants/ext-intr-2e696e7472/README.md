# 0172 Dylan — variante `.intr`

Ruolo: Interfaccia Melange Dylan che importa una funzione da un header C. Forma testuale originale basata sulla sezione Basic Use della documentazione Melange; il companion C implementa il saluto.

Tipo variante: **adapted**. Modello di partenza: examples/#172 Dylan/hello.dylan; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
melange hello.intr <output>/hello.dylan; cc -c greeting.c -o <output>/greeting.o; compilare i binding generati e collegare l’oggetto nel progetto Dylan/Mindy compatibile; invocare il binding della funzione hello_world.
```

Risultato atteso: Melange genera i binding per hello_world; il consumer Dylan collegato invoca la funzione C e stampa Hello, World!.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://opendylan.org/getting-started-cli/hello-world.html](https://opendylan.org/getting-started-cli/hello-world.html)
- [https://opendylan.org/library-reference/io/format-out.html](https://opendylan.org/library-reference/io/format-out.html)
- [https://opendylan.org/download/index.html](https://opendylan.org/download/index.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://www.cs.cmu.edu/~gwydion/dylan-release/docs/omaker-out/melange.htm](https://www.cs.cmu.edu/~gwydion/dylan-release/docs/omaker-out/melange.htm)
- [https://package.opendylan.org/melange/introduction.html](https://package.opendylan.org/melange/introduction.html)
