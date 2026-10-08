# #009 AL

L'estensione Business Central contiene un codeunit originale che mostra
`Hello, World!` e una pagina Card che lo richiama quando viene aperta.
`app.json` identifica il progetto e usa il runtime AL 14.0, compatibile con
Business Central 25. Gli oggetti pagina e codeunit hanno entrambi ID 50100;
appartengono a categorie diverse.

## Toolchain e comandi

Servono l'estensione Microsoft AL Language per Visual Studio Code, il suo
compilatore `alc.exe`, i simboli Business Central 25 e una sandbox compatibile.
Aprire questa cartella in VS Code, configurare la sandbox in `.vscode/launch.json`
e usare **AL: Download Symbols**. Compilazione dalla cartella dell'esempio,
con `alc.exe` nel PATH:

```powershell
alc.exe /project:. /packagecachepath:.alpackages /out:hello.app
```

Per pubblicare solo nella propria sandbox, usare **AL: Publish without debugging**.
Aprire la pagina **Corpus Hello** dalla ricerca del client Business Central,
oppure dall'URL della sandbox aggiungendo `?page=50100` (o `&page=50100` se
l'URL contiene già parametri). Il risultato atteso è il dialogo `Hello, World!`.

## Stato

Creato; sintassi e semantica **non verificate**. Compilatore AL, cache dei simboli
e sandbox Business Central non sono disponibili nella sessione. Nessun accesso
o pubblicazione remota è stato eseguito. Vedere `verification.log`.

## Fonti primarie

- [Microsoft: oggetto codeunit](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-codeunit-object)
- [Microsoft: Message](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/methods-auto/dialog/dialog-message-method)
- [Microsoft: manifest e launch.json](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-json-files)
- [Microsoft: versioni runtime AL](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-choosing-runtime)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.al` | [Hello.Codeunit.al](Hello.Codeunit.al), [Hello.Page.al](Hello.Page.al) creato, verifiche pendenti |
