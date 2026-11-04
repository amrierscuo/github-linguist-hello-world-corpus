# 0800: Yacc: `.yy`

Textual variation of the same format, with canon suffix .yy.

Origin: copy of the original `examples/#800 Yacc/hello.y` file.

Artefatto principale: `hello.yy`.

Control provided, from the folder of the variant:

```text
bison -d -o work/hello.tab.c hello.yy
flex -o work/lex.yy.c lexer.l
gcc work/hello.tab.c work/lex.yy.c -o work/hello
work/hello < input.txt
```

Expected result: Recognized fixtures, exit0 and Hello, World! on stdout..

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.gnu.org/software/bison/manual/bison.html](https://www.gnu.org/software/bison/manual/bison.html)
