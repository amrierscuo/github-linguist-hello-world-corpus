# 0063 BibTeX — variante `.bibtex`

Ruolo: Database BibTeX testuale, non file AUX o stile BST.

Tipo variante: **alias**. Copia byte-identica di examples/#063 BibTeX/hello.bib

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Copiare il driver AUX in output esterno, indirizzare \bibdata a hello.bibtex; bibtex sul driver.
```

Risultato atteso: driver.bbl contiene il titolo {Hello, World!}; exit 0.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://ctan.org/pkg/bibtex](https://ctan.org/pkg/bibtex)
- [https://mirrors.ctan.org/biblio/bibtex/base/btxdoc.pdf](https://mirrors.ctan.org/biblio/bibtex/base/btxdoc.pdf)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
