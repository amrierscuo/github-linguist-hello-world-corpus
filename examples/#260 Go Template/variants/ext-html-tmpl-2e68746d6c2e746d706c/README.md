# 0260 Go Template — variante `.html.tmpl`

Ruolo: Template Go con define/template e interpolazione; suffisso convenzionale della vista, nessun motore template di altri linguaggi.

Tipo variante: **alias**. Copia byte-identica di examples/#260 Go Template/hello.gotmpl

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Go html/template: ParseFiles("hello.html.tmpl"); Execute con Recipient="World"; confrontare Hello, World!.
```

Risultato atteso: World produce Hello, World! più newline; <world> produce Hello, &lt;world&gt;! più newline.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://pkg.go.dev/html/template](https://pkg.go.dev/html/template)
- [https://pkg.go.dev/text/template#hdr-Actions](https://pkg.go.dev/text/template#hdr-Actions)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
