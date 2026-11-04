# #070 BlitzBasic

Canonical entry from the corpus's `reference/languages.yml`. The reference and its order remain unchanged. The source was written for this example.

## Goal

Eseguire Print in BlitzBasic e visualizzare Hello, World!.

The .bb extension is shared with BitBake, but this file uses the syntax BASIC of Blitz3D. The source does not require graphics, media or external resources.

## Toolchain and reproduction

Blitz3D/BlitzBasic official for Windows; actual version to record

Command from the example folder, with the toolchain indicated available in the PATH. Run the build in a temporary copy to keep the generated files out of the corpus.

```text
Aprire hello.bb nell’IDE Blitz3D e usare Build and Run (F5).
```

```text
Eseguire il programma dalla stessa operazione dell’IDE.
```

## Expected result and status

The output window shows Hello, World!; finished program with End.

Artifact created: yes. syntax verified: no. behavior verified: no.

The source is documented; no native parser or runtime has been performed for this item.

Commitments: Compilatore/IDE Blitz3D unavailable; build and visual output remain to be verified in the original software.

## Primary sources

- https://blitzresearch.itch.io/blitz3d
- https://github.com/blitz-research/blitz3d

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bb` | [hello.bb](hello.bb), [consumer.bb](variants/ext-decls-2e6465636c73/consumer.bb) created; verification pending |
| `.decls` | [hello.decls](variants/ext-decls-2e6465636c73/hello.decls) created; verification pending |
