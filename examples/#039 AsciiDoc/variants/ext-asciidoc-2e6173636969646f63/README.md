# 0039 AsciiDoc — variante `.asciidoc`

Ruolo: Alias testuale dello stesso formato e dello stesso programma/dataset del modello originale.

Tipo variante: **alias**. Copia byte-identica di examples/#039 AsciiDoc/hello.adoc

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
asciidoctor hello.asciidoc -o <output>/hello.html
```

Risultato atteso: Titolo Greeting, esattamente un paragrafo Hello, World!, HTML contiene <p>Hello, World!</p>, zero diagnostiche ed exit 0.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://docs.asciidoctor.org/asciidoc/latest/](https://docs.asciidoctor.org/asciidoc/latest/)
- [https://docs.asciidoctor.org/asciidoctor.js/latest/setup/migration-guide/](https://docs.asciidoctor.org/asciidoctor.js/latest/setup/migration-guide/)
- [https://docs.asciidoctor.org/asciidoctor.js/3.0/processor/logging-api/](https://docs.asciidoctor.org/asciidoctor.js/3.0/processor/logging-api/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
