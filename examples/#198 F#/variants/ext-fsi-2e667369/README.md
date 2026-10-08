# 0198 F# — variante `.fsi`

Ruolo: Signature F# fsi, che vincola la unità di implementazione omonima.

Tipo variante: **adapted**. Modello di partenza: examples/#198 F#/hello.fsx; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
F# compiler: compilare Greeting.fsi, Greeting.fs, Program.fs in questo ordine nel progetto esterno; eseguire.
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

- [https://learn.microsoft.com/en-us/dotnet/fsharp/get-started/get-started-command-line](https://learn.microsoft.com/en-us/dotnet/fsharp/get-started/get-started-command-line)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://learn.microsoft.com/en-us/dotnet/fsharp/language-reference/signature-files](https://learn.microsoft.com/en-us/dotnet/fsharp/language-reference/signature-files)
