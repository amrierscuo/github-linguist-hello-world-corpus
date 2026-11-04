# 0562: Protocol Buffer Text Format: `.pbt`

Textual variation of the same format, with canon suffix .pbt.

Origin: copy of the original `examples/#562 Protocol Buffer Text Format/hello.textproto` file.

Artefatto principale: `hello.pbt`.

Control provided, from the folder of the variant:

```text
Prerequisiti: protoc e runtime Python google.protobuf compatibili, disponibili in toolchain isolata.
mkdir -p /absolute/work/protobuf-build
protoc --proto_path=. --python_out=/absolute/work/protobuf-build hello.proto
python verify.py /absolute/work/protobuf-build
```

Expected result: Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://protobuf.dev/programming-guides/proto3/](https://protobuf.dev/programming-guides/proto3/)
- [https://protobuf.dev/reference/protobuf/textformat-spec/](https://protobuf.dev/reference/protobuf/textformat-spec/)
