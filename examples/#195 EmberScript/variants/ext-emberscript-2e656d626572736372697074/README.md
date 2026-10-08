# 0195 EmberScript — variante `.emberscript`

Ruolo: Alias testuale dello stesso formato e dello stesso programma/dataset del modello originale.

Tipo variante: **alias**. Copia byte-identica di examples/#195 EmberScript/hello.em

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
EmberScript compiler originale: compilare hello.emberscript e lanciare il JavaScript generato.
```

Risultato atteso: stdout `Hello, World!\n`, uscita 0.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://github.com/ghempton/ember-script](https://github.com/ghempton/ember-script)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
