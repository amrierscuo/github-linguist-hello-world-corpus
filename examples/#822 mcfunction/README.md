# #822 mcfunction

Scrivere il saluto nello storage di un datapack Minecraft Java.

## Toolchain

Minecraft Java command parser/runtime

## Procedura

Inserire hello.mcfunction in un datapack compatibile; eseguire /function corpus:hello e /data get storage corpus:hello greeting.

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.

Il goal è una stringa locale nello storage del mondo di prova, senza messaggi chat o connessioni esterne.

Requisiti residui:
- Minecraft Java runtime/datapack di prova non disponibile.

## Fonti primarie

- [https://minecraft.wiki/w/Commands/data](https://minecraft.wiki/w/Commands/data)
- [https://www.minecraft.net/en-us/article/minecraft-java-edition-1-21](https://www.minecraft.net/en-us/article/minecraft-java-edition-1-21)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mcfunction` | [hello.mcfunction](hello.mcfunction) creato, verifiche pendenti |
