# 0333 — Java: `.jav`

Ruolo: Alias storico di sorgente Java; javac richiede il nome hello.java per la classe pubblica.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#333 Java/hello.java.

Toolchain richiesta: OpenJDK 21.0.12. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Copiare hello.jav in una directory di build come hello.java; javac hello.java; java Hello
```

Risultato atteso: stdout Hello, World! e LF, uscita 0.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.jav`: `e8533e4508f5734f52cbfcf23d34a842fcce5d27f9d82b23ca2f4ff6b3bf1e32`

Fonti primarie:

- https://docs.oracle.com/javase/tutorial/getStarted/cupojava/win32.html
