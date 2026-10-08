# 0029 AngelScript — variante `.angelscript`

Ruolo: Alias testuale dello stesso formato e dello stesso programma/dataset del modello originale.

Tipo variante: **alias**. Copia byte-identica di examples/#029 AngelScript/hello.as

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
AngelScript host originale: compilare e invocare la funzione del file hello.angelscript con lo stesso engine del modello.
```

Risultato atteso: Compilazione bytecode e VM: exit 0; stdout esattamente Hello, World! seguito da newline.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://www.angelcode.com/angelscript/sdk/docs/manual/doc_samples_asrun.html](https://www.angelcode.com/angelscript/sdk/docs/manual/doc_samples_asrun.html)
- [https://github.com/anjo76/angelscript/releases/tag/v2.38.0](https://github.com/anjo76/angelscript/releases/tag/v2.38.0)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
