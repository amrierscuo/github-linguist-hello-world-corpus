# #155 DM

The canonical entry and order come from the corpus's `reference/languages.yml`. Sources and fixtures are original; any dumps or bundles come from the stated tools.

## Goal

Fill out a world BYOND DM that writes Hello, World! on the log server and stops.

hello.dm redefines /world/New(), recalls..() and uses the output of the world. hello.dme includes the source for DreamMaker. The goal is a short local server startup, without maps, clients or graphic resources.

## Toolchain and reproduction

BYOND DreamMaker e DreamDaemon; versioni effettive da registrare

Commands in the example folder with the toolchain available in PATH. Use a temporary copy: databases, objects, audio and other test outputs do not belong to the corpus.

```text
DreamMaker hello.dme
```

```text
DreamDaemon hello.dmb -trusted -close
```

## Expected result and status

world.log shows Hello, World! during /world/New(); shutdown() concludes the world.

Artifact created: yes. syntax verified: no. behavior verified: no.

The source is documented; native parser/compilatore/runtime has not been performed for this item.

Impedimenti: Toolchain BYOND non preparata; compilazione DM e runtime DreamDaemon restano da eseguire.

## Primary sources

- https://www.byond.com/docs/guide/chap08.html
- https://www.byond.com/docs/ref/contents.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.dm` | [hello.dm](hello.dm) created; verification pending |
