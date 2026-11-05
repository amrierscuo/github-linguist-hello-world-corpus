# 0808: Zimpl: `.zimpl`

## Latest recorded verification

**Syntax and behavior verified** for `.zimpl`. After explicitly binding the indexed-variable iterator in the three declared sources, native Zimpl generated each LP and GLPK solved it to optimality. The thirteen native solution variables decode to exactly Hello, World!. Each suffix was compiled and solved separately. [Recorded evidence](../../verification/native_20261105_batch_main.json).

Textual variation of the same format, with canon suffix .zimpl.

Origin: copy of the original `examples/#808 Zimpl/hello.zpl` file.

Artefatto principale: `hello.zimpl`.

Control provided, from the folder of the variant:

```text
zimpl -o work/hello hello.zimpl
```

Expected result: Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://zimpl.zib.de/](https://zimpl.zib.de/)
