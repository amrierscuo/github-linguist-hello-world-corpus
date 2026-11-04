# #777 World of Warcraft Addon Data

Voce canonica `World of Warcraft Addon Data`, tipo `data`, language_id `396`.

Addon World of Warcraft original: TOC Greeting.toc declares title and version and charge Greeting.lua, which prints `Hello, World!`.

## Toolchain and reproduction

World of Warcraft native addon loader, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

The Interface 110200 field declares a 11.2.0 retail target, not a pretext for compatibility with any future version. For other clients, please explicitly update that target and check with the client loader. Source: Blizzard original UI sources distributed in the mirror indicated.

Comando/procedura from the directory of the example, unless explicit indications:

```text
Nel client compatibile, collocare Greeting.toc e Greeting.lua in Interface/AddOns/Greeting; abilitare l’addon; ricaricare l’interfaccia e osservare il saluto nella chat.
```

Expected result: Loader accepts Greeting.toc, charge Greeting.lua and appears Hello, World! in the chat.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

The TOC title and the script have a real purpose, but only one Lua test would not wait for the TOC loading: both flags remain false.

Remaining requirements:

- Client World of Warcraft e caricatore addon assenti; metadata TOC e script sono creati, caricamento non provato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/Gethe/wow-ui-source](https://github.com/Gethe/wow-ui-source)
- [https://raw.githubusercontent.com/Gethe/wow-ui-source/live/Interface/AddOns/Blizzard_APIDocumentation/Blizzard_APIDocumentation.toc](https://raw.githubusercontent.com/Gethe/wow-ui-source/live/Interface/AddOns/Blizzard_APIDocumentation/Blizzard_APIDocumentation.toc)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.toc` | [Greeting.toc](Greeting.toc) created; verification pending |
