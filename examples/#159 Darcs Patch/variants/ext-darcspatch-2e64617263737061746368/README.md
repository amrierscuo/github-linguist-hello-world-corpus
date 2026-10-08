# 0159 Darcs Patch — variante `.darcspatch`

Ruolo: Alias testuale dello stesso formato e dello stesso programma/dataset del modello originale.

Tipo variante: **alias**. Copia byte-identica di examples/#159 Darcs Patch/hello.dpatch

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Darcs in repository temporaneo della fixture: darcs apply --dry-run hello.darcspatch; applicare nel repo temporaneo e leggere greeting.txt.
```

Risultato atteso: Applicazione exit 0 e greeting.txt esattamente Hello, World! seguito da newline.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://darcs.net/Using/Commands](https://darcs.net/Using/Commands)
- [https://darcs.net/Using/Send](https://darcs.net/Using/Send)
- [https://darcs.net/Binaries](https://darcs.net/Binaries)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
