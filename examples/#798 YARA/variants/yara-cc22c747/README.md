# 0798: YARA: `.yara`

## Latest recorded verification

**Syntax and behavior verified** for `.yara`. YARA: compile the original rules, match the exact declared greeting.txt (including its trailing LF), and reject a separate Hello, Moon! fixture. [Recorded evidence](../../verification/native_20261104_followup_2e79617261.json).

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
