# #211 FlatBuffers

Voce canonica `FlatBuffers`, tipo `data`, language_id `577640576`.

Define the FlatBuffers Greeting scheme and codificare/decodificare a JSON message with HELO binary identifier.

## Toolchain and reproduction

Official FlatBuffers flatc binary schema compiler and codec, flatc version 25.12.19. Test environment: **Windows x64**.

official flatc 25.12.19 portable Windows x64. Use a separate build folder; schema, JSON original and log are the only artifacts included.

Comando/procedura from the directory of the example, unless explicit indications:

```text
flatc --binary --strict-json -o build hello.fbs greeting.json; flatc --json --strict-json -o build hello.fbs -- build/greeting.bin
```

Expected result: JSON decoded { "message": "Hello, World!" }; HELO identifier; exit 0.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

La prova verifica il JSON decodificato esatto, il campo message e l’identificatore HELO ai byte 4..7 del vero FlatBuffer. L’hash del binario temporaneo è nel log.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sources verified in staging. The only available probe do not attest parsing
or execution. Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://flatbuffers.dev/schema/](https://flatbuffers.dev/schema/)
- [https://flatbuffers.dev/flatc/](https://flatbuffers.dev/flatc/)
- [https://github.com/google/flatbuffers/releases](https://github.com/google/flatbuffers/releases)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.fbs` | [hello.fbs](hello.fbs) verified |
