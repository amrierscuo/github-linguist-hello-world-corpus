# 0244 Gettext Catalog — variante `.pot`

Ruolo: Template gettext POT: msgid contiene il testo sorgente e msgstr è vuoto, distinto dal catalogo PO tradotto.

Tipo variante: **adapted**. Modello di partenza: examples/#244 Gettext Catalog/hello.po; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
msgfmt --check --check-format hello.pot -o <output>/template.mo; gettext reader: controllare il msgid Hello, World! e la traduzione ancora vuota.
```

Risultato atteso: Catalogo template valido; msgid Hello, World! non tradotto.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html)
- [https://www.gnu.org/software/gettext/manual/html_node/msgfmt-Invocation.html](https://www.gnu.org/software/gettext/manual/html_node/msgfmt-Invocation.html)
- [https://docs.python.org/3/library/gettext.html](https://docs.python.org/3/library/gettext.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
