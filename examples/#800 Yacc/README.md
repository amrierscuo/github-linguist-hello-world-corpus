# #800 Yacc

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Generare un parser Yacc e riconoscere il saluto della fixture.

Bison genera il parser dalla grammatica .y; Flex genera il lexer originale complementare. Il parser compilato legge input.txt ed esegue l’azione solo dopo riconoscimento.

## Toolchain e riproduzione

GNU Bison3.8.2 compatibile Yacc, Flex2.6.4, M4 e GCC originali

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
bison -d hello.y; flex lexer.l; gcc hello.tab.c lex.yy.c -o hello; ./hello < input.txt
```

## Risultato atteso e stato

Fixture riconosciuta, exit0 e Hello, World! su stdout.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.gnu.org/software/bison/manual/bison.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.y` | [hello.y](hello.y) verificato |
| `.yacc` | [hello.yacc](variants/yacc-a86b8c02/hello.yacc) creato, verifiche pendenti |
| `.yy` | [hello.yy](variants/yy-d3b03e84/hello.yy) creato, verifiche pendenti |
