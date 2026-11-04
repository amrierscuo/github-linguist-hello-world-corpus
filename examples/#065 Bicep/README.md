# #065 Bicep

Canonical entry from the corpus's `reference/languages.yml`. The reference and its order remain unchanged. The source was written for this example.

## Goal

Fill out an output Bicep constant greeting = Hello, World!.

The verification runs the compiler and controls the output ARM generated. It does not require Azure credentials or resource distribution.

## Toolchain and reproduction

Microsoft Bicep CLI 0.48.1, Windows x64 ufficiale

Command from the example folder, with the toolchain indicated available in the PATH. Run the build in a temporary copy to keep the generated files out of the corpus.

```text
bicep build hello.bicep --outfile hello.json
```

```text
Controllare hello.json: outputs.greeting == {"type":"string","value":"Hello, World!"}.
```

## Expected result and status

Exit 0 and output ARM JSON exactly the same as the constant request.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records actual commands, versioni/provenienza of the toolchain, output codes, stdout/stderr and SHA-256 of the proven sources.

## Primary sources

- https://learn.microsoft.com/azure/azure-resource-manager/bicep/outputs
- https://github.com/Azure/bicep/releases

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bicep` | [hello.bicep](hello.bicep), [main.bicep](variants/ext-bicepparam-2e6269636570706172616d/main.bicep) created; verification pending |
| `.bicepparam` | [hello.bicepparam](variants/ext-bicepparam-2e6269636570706172616d/hello.bicepparam) created; verification pending |
