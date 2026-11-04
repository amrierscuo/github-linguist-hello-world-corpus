# #036 AppleScript

Restituire la stringa Hello, World! dallo script AppleScript e farla mostrare da osascript su stdout.

## File

- `hello.applescript`

## Toolchain and verification

macOS with AppleScript, osacompile and osascript system; version to be recorded during macOS test.

Run on macOS from the example folder:

```sh
sw_vers
osacompile -o /tmp/hello.scpt hello.applescript
osascript hello.applescript
```

`return` returns the string to the caller; `osascript` makes the result on
stdout. The separate compilation serves to distinguish control of syntax
dall'esecuzione. Registrare versione macOS/AppleScript, codici di uscita e
stdout. No external applications or events sent to other apps are required.

## Expected result

Compilazione exit 0. osascript: exit 0 e stdout esattamente Hello, World! seguito da newline.

## State of the test

Syntax and behavioral verification pending.

Source compared with Apple documentation. Manual consultation is not a syntax or runtime verification.

Remaining requirements:
- Ambiente corrente Windows: runtime AppleScript/macOS unavailable; nessun parser o interprete AppleScript eseguito.

## Primary sources

- [https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_handlers.html](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_handlers.html)
- [https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.applescript` | [hello.applescript](hello.applescript) created; verification pending |
| `.scpt` | [hello.scpt](variants/ext-scpt-2e73637074/hello.scpt) created; verification pending |
