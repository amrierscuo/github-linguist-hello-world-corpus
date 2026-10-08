# #164 DenizenScript

Eseguire un task DenizenScript che annuncia Hello, World! nella console del server.

## Toolchain

Denizen plugin su server Minecraft/Paper compatibile; versioni effettive da registrare

## Comandi e procedura

Copiare hello.dsc in plugins/Denizen/scripts; eseguire /ex reload e /ex run hello_world

## Risultato atteso

Reload senza errori; task hello_world scrive Hello, World! nella console.

## Stato

Sintassi e semantica in attesa.

announce to_console evita il requisito di un player destinatario. La struttura è un task Denizen reale; un parser YAML da solo non attesterebbe i comandi del plugin.

Requisiti residui:
- Server Minecraft/Paper e plugin Denizen compatibile non disponibili; reload e task non eseguiti.

## Fonti primarie e riferimento di formato

- [https://guide.denizenscript.com/guides/first-steps/task-script.html](https://guide.denizenscript.com/guides/first-steps/task-script.html)
- [https://meta.denizenscript.com/Docs/Commands/Announce](https://meta.denizenscript.com/Docs/Commands/Announce)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.dsc` | [hello.dsc](hello.dsc) creato, verifiche pendenti |
