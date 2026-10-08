# 0219 FreeMarker — variante `.ftlh`

Ruolo: Template FreeMarker HTML con output format e autoescaping espliciti.

Tipo variante: **adapted**. Modello di partenza: examples/#219 FreeMarker/hello.ftl; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
FreeMarker Configuration: caricare hello.ftlh e processare con name="World"; controllare il paragrafo HTML.
```

Risultato atteso: <p>Hello, World!</p>

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://freemarker.apache.org/docs/dgui_quickstart_basics.html](https://freemarker.apache.org/docs/dgui_quickstart_basics.html)
- [https://freemarker.apache.org/docs/pgui_quickstart_all.html](https://freemarker.apache.org/docs/pgui_quickstart_all.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://freemarker.apache.org/docs/dgui_misc_autoescaping.html](https://freemarker.apache.org/docs/dgui_misc_autoescaping.html)
