# #561 Protocol Buffer

Fill out the Protocol Buffer scheme and leggere/serializzare text message.

## Toolchain

libprotoc 3.21.12; CPython 3.13.9; google.protobuf 5.29.3

## Procedure

protoc --python_out=build hello.proto; python verify.py build

## Expected result

Hello, World!

## Status

syntax and behavior verified.

The original compiler generates the Python module only in work; the real text_format parser reads the message, then the runtime serializes and deserializes the field.

Real check 2026-10-08T13:16:51.728386+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://protobuf.dev/programming-guides/proto3/](https://protobuf.dev/programming-guides/proto3/)
- [https://protobuf.dev/reference/protobuf/textformat-spec/](https://protobuf.dev/reference/protobuf/textformat-spec/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.proto` | [hello.proto](hello.proto) verified |
