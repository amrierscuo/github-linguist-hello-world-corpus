# 0058 Batchfile — variante `.bat`

Ruolo: Alias testuale dello stesso formato e dello stesso programma/dataset del modello originale.

Tipo variante: **alias**. Copia byte-identica di examples/#058 Batchfile/hello.cmd

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
cmd.exe /d /c hello.bat
```

Risultato atteso: Exit 0; stdout Hello, World! seguito da CRLF.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://learn.microsoft.com/windows-server/administration/windows-commands/echo](https://learn.microsoft.com/windows-server/administration/windows-commands/echo)
- [https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
