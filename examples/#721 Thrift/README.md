# #721 Thrift

Fill in a Thrift structure and keep the constant greeting.

## Toolchain

Thrift version 0.19.0

## Procedure

thrift --gen py -out build hello.thrift; controllare corpus/constants.py generato con HELLO.

## Expected result

Hello, World!

## Status

syntax and behavior verified.

The original compiler generates Python; the verification reads the real constant from the generated module.

Real check 2026-10-08T13:30:04.884795+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://thrift.apache.org/docs/idl](https://thrift.apache.org/docs/idl)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.thrift` | [hello.thrift](hello.thrift) verified |
