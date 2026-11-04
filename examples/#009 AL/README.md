# #009 AL

The Business Central extension contains an original codeunit showing
`Hello, World!` and a Card page that recalls it when opened.
`app.json` identifies the project and uses AL 14.0 runtime, compatible with
Business Central 25. The page and codeunit objects both have ID 50100;
appartengono a categorie diverse.

## Toolchain and commands

Need Microsoft AL Language extension for Visual Studio Code, its
`alc.exe` compiler, Business Central 25 symbols and a compatible sandbox.
Open this folder in VS Code, configure sandbox in `.vscode/launch.json`
and use **AL: Download Symbols**. Filling from the example folder,
with `alc.exe` in PATH:

```powershell
alc.exe /project:. /packagecachepath:.alpackages /out:hello.app
```

To publish only in your sandbox, use **AL: Publish without debugging**.
Open the **Corpus Hello** page from search for Business Central client,
or from the sandbox URL by adding `?page=50100` (or `&page=50100` if
the URL already contains parameters). The expected result is the `Hello, World!` dialogue.

## Status

created; syntax e behavior **non verificate**. Compilatore AL, cache dei simboli
and Sandbox Business Central are not available in the session. No access
or remote publication has been executed. See `verification.log`.

## Primary sources

- [Microsoft: oggetto codeunit](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-codeunit-object)
- [Microsoft: Message](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/methods-auto/dialog/dialog-message-method)
- [Microsoft: manifest e launch.json](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-json-files)
- [Microsoft: versioni runtime AL](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-choosing-runtime)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.al` | [Hello.Codeunit.al](Hello.Codeunit.al), [Hello.Page.al](Hello.Page.al) created; verification pending |
