# 0416 — Makefile: `.d`

Ruolo: Make dependency fragment: relazione hello.o: hello.c, include dal Makefile di supporto.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: GNU Make on Ubuntu 24.04. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
make -f Makefile; ./hello
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `true`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Nessun impedimento per l’ambito effettivamente verificato.

SHA-256 dei file della variante:

- `Makefile`: `c48a2b7ba6f1ee0a439b1d28d4aa194b79635e80ccab6cc9d6411f906d10804e`
- `hello.c`: `ed022c4313ef7444150bc047da163dd09eb5ae942093b1e6c97e1cf32dfbad7a`
- `hello.d`: `6d8c2cb1c59f2480bbaaa17229e7f4d43e458e8b7a44f4bfdc17cd316bc11be6`

Fonti primarie:

- https://www.gnu.org/software/make/manual/html_node/Automatic-Prerequisites.html
- https://www.gnu.org/software/make/manual/html_node/Recipes.html

Prova aggiuntiva realmente eseguita:

Make originale include il frammento dipendenze .d; GCC compila il fixture; binario eseguito nel work, stdout esatto Hello, World! e LF.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: [{'command': ['wsl', '--exec', 'make', '--version'], 'exit_code': 0, 'stdout': 'GNU Make 4.3\nBuilt for x86_64-pc-linux-gnu\nCopyright (C) 1988-2020 Free Software Foundation, Inc.\nLicense GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>\nThis is free software: you are free to change and redistribute it.\nThere is NO WARRANTY, to the extent permitted by law.\n', 'stderr': ''}, {'command': ['wsl', '--exec', 'gcc', '--version'], 'exit_code': 0, 'stdout': 'gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0\nCopyright (C) 2023 Free Software Foundation, Inc.\nThis is free software; see the source for copying conditions.  There is NO\nwarranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n\n', 'stderr': ''}]
