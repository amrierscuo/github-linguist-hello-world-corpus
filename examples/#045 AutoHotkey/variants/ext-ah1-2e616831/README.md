# 0045 AutoHotkey — variante `.ah1`

Ruolo: Script AutoHotkey v1; sintassi command, non funzioni v2.

Tipo variante: **adapted**. Modello di partenza: examples/#045 AutoHotkey/hello.ahk; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
AutoHotkeyU64.exe /ErrorStdOut hello.ah1
```

Risultato atteso: Hello, World!

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://github.com/AutoHotkey/AutoHotkeyDocs/blob/v2/docs/lib/FileAppend.htm](https://github.com/AutoHotkey/AutoHotkeyDocs/blob/v2/docs/lib/FileAppend.htm)
- [https://www.autohotkey.com/download/2.0/](https://www.autohotkey.com/download/2.0/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://www.autohotkey.com/docs/v1/lib/FileAppend.htm](https://www.autohotkey.com/docs/v1/lib/FileAppend.htm)
