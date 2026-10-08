# #036 AppleScript

Restituire la stringa Hello, World! dallo script AppleScript e farla mostrare da osascript su stdout.

## File

- `hello.applescript`

## Toolchain e verifica

macOS con AppleScript, osacompile e osascript di sistema; versione da registrare durante la prova macOS.

Eseguire su macOS dalla cartella dell'esempio:

```sh
sw_vers
osacompile -o /tmp/hello.scpt hello.applescript
osascript hello.applescript
```

`return` restituisce la stringa al chiamante; `osascript` rende il risultato su
stdout. La compilazione separata serve a distinguere il controllo di sintassi
dall'esecuzione. Registrare versione macOS/AppleScript, codici di uscita e
stdout. Non sono necessarie applicazioni esterne o eventi inviati ad altre app.

## Risultato atteso

Compilazione exit 0. osascript: exit 0 e stdout esattamente Hello, World! seguito da newline.

## Stato della prova

Sintassi e semantica in attesa.

Sorgente confrontata con la documentazione Apple. La consultazione del manuale non è una verifica di sintassi o runtime.

Requisiti residui:
- Ambiente corrente Windows: runtime AppleScript/macOS non disponibile; nessun parser o interprete AppleScript eseguito.

## Fonti primarie

- [https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_handlers.html](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_handlers.html)
- [https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.applescript` | [hello.applescript](hello.applescript) creato, verifiche pendenti |
| `.scpt` | [hello.scpt](variants/ext-scpt-2e73637074/hello.scpt) creato, verifiche pendenti |
