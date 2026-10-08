# 0045 AutoHotkey — variante `.ahkl`

Ruolo: Script AutoHotkey v2 con #Requires esplicito; suffisso .ahkl del sorgente.

Tipo variante: **alias**. Copia byte-identica di examples/#045 AutoHotkey/hello.ahk

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
AutoHotkey64.exe /ErrorStdOut hello.ahkl
```

Risultato atteso: Exit 0; stdout catturato esattamente Hello, World! seguito da LF.

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
