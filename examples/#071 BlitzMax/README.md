# #071 BlitzMax

Canonical entry from the corpus's `reference/languages.yml`. The reference and its order remain unchanged. The source was written for this example.

## Goal

Fill out a BlitzMax console application with BRL.StandardIO and print Hello, World!.

SuperStrict enables strict checking. Framework BRL.StandardIO provides console output. No graphics dependencies are required.

## Toolchain and reproduction

BlitzMax NG con bmk e modulo BRL.StandardIO; versione effettiva da registrare

Command from the example folder, with the toolchain indicated available in the PATH. Run the build in a temporary copy to keep the generated files out of the corpus.

```text
bmk makeapp -t console -o hello hello.bmx
```

```text
./hello (su Windows: hello.exe)
```

## Expected result and status

stdout Hello, World! seguito da newline; exit 0.

Artifact created: yes. syntax verified: no. behavior verified: no.

The source is documented; no native parser or runtime has been performed for this item.

Impedimenti: BlitzMax NG/bmk unavailable; compilazione ed esecuzione restano da verificare.

## Primary sources

- https://blitzmax.org/docs/en/setup/get_started/
- https://blitzmax.org/docs/en/api/brl/brl.standardio/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bmx` | [hello.bmx](hello.bmx) created; verification pending |
