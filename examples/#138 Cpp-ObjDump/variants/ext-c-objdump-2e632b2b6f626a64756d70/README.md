# 0138 Cpp-ObjDump — variante `.c++objdump`

Ruolo: Disassembly objdump testuale autentico del programma C++ già presente: solo alias del formato, non codice C++ compilabile.

Tipo variante: **alias**. Copia byte-identica di examples/#138 Cpp-ObjDump/hello.cppobjdump

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Rigenerare disassembly con objdump -d -C sul binario C++ originale in output esterno e confrontare con hello.c++objdump.
```

Risultato atteso: Dump ELF x86_64 con <main>: e sezione .rodata; strings individua Hello, World!; l’eseguibile termina 0 con il saluto.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://sourceware.org/binutils/docs/binutils/objdump.html](https://sourceware.org/binutils/docs/binutils/objdump.html)
- [https://sourceware.org/binutils/docs/binutils/strings.html](https://sourceware.org/binutils/docs/binutils/strings.html)
- [https://gcc.gnu.org/onlinedocs/gcc/Invoking-G_002b_002b.html](https://gcc.gnu.org/onlinedocs/gcc/Invoking-G_002b_002b.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
