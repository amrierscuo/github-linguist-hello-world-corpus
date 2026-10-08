# #562 Protocol Buffer Text Format

Compilare lo schema Protocol Buffer e leggere/serializzare il messaggio di testo.

## Toolchain

libprotoc 3.21.12; CPython 3.13.9; google.protobuf 5.29.3

## Procedura

protoc --python_out=build hello.proto; python verify.py build

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

Il compilatore originale genera il modulo Python soltanto in work; il parser text_format reale legge il messaggio, poi il runtime serializza e deserializza il campo.

Verifica reale 2026-10-08T13:16:51.728488+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://protobuf.dev/programming-guides/proto3/](https://protobuf.dev/programming-guides/proto3/)
- [https://protobuf.dev/reference/protobuf/textformat-spec/](https://protobuf.dev/reference/protobuf/textformat-spec/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.textproto` | [hello.textproto](hello.textproto) verificato |
| `.pbt` | [hello.pbt](variants/pbt-c9751eff/hello.pbt) creato, verifiche pendenti |
| `.pbtxt` | [hello.pbtxt](variants/pbtxt-2f9cd8d4/hello.pbtxt) creato, verifiche pendenti |
| `.txtpb` | [hello.txtpb](variants/txtpb-021d97e9/hello.txtpb) creato, verifiche pendenti |
