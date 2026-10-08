# 0084 C# — variante `.cs.pp`

Ruolo: Template di preprocessamento NuGet, con token rootnamespace da sostituire prima della compilazione.

Tipo variante: **adapted**. Modello di partenza: examples/#084 C#/Hello.cs; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
NuGet content transform: sostituire $rootnamespace$ con Corpus in un progetto temporaneo; compilare il C# risultante ed eseguirlo.
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

- [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-options/](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-options/)
- [https://learn.microsoft.com/en-us/dotnet/api/system.console.writeline](https://learn.microsoft.com/en-us/dotnet/api/system.console.writeline)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://learn.microsoft.com/en-us/nuget/create-packages/source-and-config-file-transformations](https://learn.microsoft.com/en-us/nuget/create-packages/source-and-config-file-transformations)
