# 0644: SWIG: `.swg`

Textual variation of the same format, with canon suffix .swg.

Origin: copy of the original `examples/#644 SWIG/hello.i` file.

Artefatto principale: `hello.swg`.

Control provided, from the folder of the variant:

```text
swig -python -outdir work -o work/hello_wrap.c hello.swg
```

Expected result: Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://swig.org/Doc4.3/SWIGDocumentation.html](https://swig.org/Doc4.3/SWIGDocumentation.html)
