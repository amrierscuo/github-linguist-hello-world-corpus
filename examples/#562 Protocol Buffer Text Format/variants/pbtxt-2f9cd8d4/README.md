# 0562 — Protocol Buffer Text Format — `.pbtxt`

Variante testuale dello stesso formato, con suffisso canonico .pbtxt.

Provenienza: copia del file originale `examples/#562 Protocol Buffer Text Format/hello.textproto`.

Artefatto principale: `hello.pbtxt`.

Controllo previsto, dalla cartella della variante:

```text
Prerequisiti: protoc e runtime Python google.protobuf compatibili, disponibili in toolchain isolata.
mkdir -p /absolute/work/protobuf-build
protoc --proto_path=. --python_out=/absolute/work/protobuf-build hello.proto
python verify.py /absolute/work/protobuf-build
```

Risultato atteso: Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://protobuf.dev/programming-guides/proto3/](https://protobuf.dev/programming-guides/proto3/)
- [https://protobuf.dev/reference/protobuf/textformat-spec/](https://protobuf.dev/reference/protobuf/textformat-spec/)
