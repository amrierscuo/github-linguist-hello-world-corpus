# 0611: Regular Expression: `.regex`

Textual variation of the same format, with canon suffix .regex.

Origin: copy of the original `examples/#611 Regular Expression/hello.regexp` file.

Artefatto principale: `hello.regex`.

Control provided, from the folder of the variant:

```text
python -c "import re,pathlib; r=re.compile(pathlib.Path('hello.regex').read_text().strip()); assert r.fullmatch('Hello, World!')"
```

Expected result: Hello, World! in output or compliant data, according to the scope described..

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)
