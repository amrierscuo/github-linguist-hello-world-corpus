# #354 Kaitai Struct

Voce canonica `Kaitai Struct`, tipo `programming`, language_id `818804755`.

Fill in a specific Kaitai Struct and read an original binary fixture with magic, length and string UTF - 8.

## Toolchain and reproduction

Official Kaitai Struct Scala compiler JavaScript build and Python runtime, compiler 0.11.0; kaitaistruct 0.11. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Compiler Kaitai Struct official 0.11.0, build JavaScript of the compiler Original scale, and runtime Python kaitaistruct 0.11. greeting.bin contains the original bytes HW, 0x0d and thirteen greeting characters.

Comando/procedura from the directory of the example, unless explicit indications:

```text
npm install --prefix .tools kaitai-struct-compiler@0.11.0 js-yaml@4.1.0; python -m pip install kaitaistruct==0.11; node compile.cjs .tools build; python verify.py build greeting.bin
```

Expected result: Magic HW, length= 13, message= Hello, World!, stream consumed; negative control and PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

La specifica è compilata dal vero compiler. Il helper importa solo il Python realmente generato in build, legge la fixture, verifica posizione finale e rifiuto di magic errato. Il parser generato e le dipendenze non sono inclusi nel corpus.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://doc.kaitai.io/user_guide.html](https://doc.kaitai.io/user_guide.html)
- [https://github.com/kaitai-io/kaitai_struct_compiler](https://github.com/kaitai-io/kaitai_struct_compiler)
- [https://doc.kaitai.io/lang_python.html](https://doc.kaitai.io/lang_python.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ksy` | [greeting.ksy](greeting.ksy) verified |
