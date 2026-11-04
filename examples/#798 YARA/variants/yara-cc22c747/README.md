# 0798: YARA: `.yara`

Textual variation of the same format, with canon suffix .yara.

Origin: copy of the original `examples/#798 YARA/hello.yar` file.

Artefatto principale: `hello.yara`.

Control provided, from the folder of the variant:

```text
yara hello.yara greeting.txt
```

Expected result: A CorpusGreeting correspondence for Hello, World!, none for Hello, Moon!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://yara.readthedocs.io/en/stable/writingrules.html](https://yara.readthedocs.io/en/stable/writingrules.html)
