# 0765: WebAssembly: `.wast`

WebAssembly spec test script with module and assertion, not only WAT renamed.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.wast`.

Control provided, from the folder of the variant:

```text
wast2json hello.wast -o work/hello.json; spectest-interp work/hello.json
```

Expected result: assert_return pass; the module keeps greeting in memory.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://github.com/WebAssembly/wabt](https://github.com/WebAssembly/wabt)
- [https://github.com/WebAssembly/spec/tree/main/interpreter](https://github.com/WebAssembly/spec/tree/main/interpreter)
