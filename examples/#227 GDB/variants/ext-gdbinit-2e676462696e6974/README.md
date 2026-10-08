# 0227 GDB — variante `.gdbinit`

Ruolo: Comandi GDB caricabili come file di inizializzazione esplicito; nessun cambio di init globale.

Tipo variante: **alias**. Copia byte-identica di examples/#227 GDB/hello.gdb

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
gdb -q -nx -batch -x hello.gdbinit
```

Risultato atteso: stdout esattamente Hello, World! seguito da newline; exit 0.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://www.gnu.org/software/gdb/documentation/](https://www.gnu.org/software/gdb/documentation/)
- [https://sourceware.org/gdb/current/onlinedocs/gdb.html/Output.html](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Output.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
