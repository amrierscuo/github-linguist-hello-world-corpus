# #234 Game Maker Language

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Run GML code in a Create event and show Hello, World! in GameMaker log.

L’artefatto è codice Game Maker Language per il contesto di un evento, con variabile locale e show_debug_message. Il file non viene dichiarato come un progetto GameMaker completo.

## Toolchain and reproduction

GameMaker IDE/runtime, versione effettiva da registrare

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
Inserire hello.gml nell’evento Create di un oggetto in una room, poi eseguire il progetto.
```

## Expected result and status

The debug log shows Hello, World! once.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no native parser/compilatore/runtime performed for this item.

Impedimenti: IDE/runtime GameMaker non preparati; parser e creazione della room/evento non verificati.

## Primary sources

- https://manual.gamemaker.io/monthly/en/GameMaker_Language/GML_Reference/Debugging/show_debug_message.htm

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gml` | [hello.gml](hello.gml) created; verification pending |
