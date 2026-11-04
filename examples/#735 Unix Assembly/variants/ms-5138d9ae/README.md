# 0735: Unix Assembly: `.ms`

Textual variation of the same format, with canon suffix .ms.

Origin: copy of the original `examples/#735 Unix Assembly/hello.s` file.

Artefatto principale: `hello.ms`.

Control provided, from the folder of the variant:

```text
as --64 hello.ms -o work/hello.o
ld work/hello.o -o work/hello
work/hello
```

Expected result: Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://sourceware.org/binutils/docs/as/](https://sourceware.org/binutils/docs/as/)
- [https://man7.org/linux/man-pages/man2/write.2.html](https://man7.org/linux/man-pages/man2/write.2.html)
