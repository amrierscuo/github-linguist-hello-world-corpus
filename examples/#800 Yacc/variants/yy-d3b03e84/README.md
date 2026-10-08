# 0800 — Yacc — `.yy`

Variante testuale dello stesso formato, con suffisso canonico .yy.

Provenienza: copia del file originale `examples/#800 Yacc/hello.y`.

Artefatto principale: `hello.yy`.

Controllo previsto, dalla cartella della variante:

```text
bison -d -o work/hello.tab.c hello.yy
flex -o work/lex.yy.c lexer.l
gcc work/hello.tab.c work/lex.yy.c -o work/hello
work/hello < input.txt
```

Risultato atteso: Fixture riconosciuta, exit0 e Hello, World! su stdout..

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://www.gnu.org/software/bison/manual/bison.html](https://www.gnu.org/software/bison/manual/bison.html)
