# #742 VBScript

Eseguire VBScript con il console script host di Windows.

Tipo canonico `programming`, language_id `408016005`.

Toolchain prevista: Windows cscript.exe e VBScript engine.

Dalla cartella dell’esempio:

```sh
cscript //nologo hello.vbs
```

Risultato atteso: stdout Hello, World! e newline.

cscript è usato in modalità console, senza dialoghi.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Windows cscript console host + original VBScript engine. [Log](verification/result.json). 

Fonti:

- [Windows Script Host](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/legacy/9bbdkx3k(v=vs.85))

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.vbs` | [hello.vbs](hello.vbs) verificato |
