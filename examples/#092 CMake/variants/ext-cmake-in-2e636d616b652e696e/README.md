# 0092 CMake — variante `.cmake.in`

Ruolo: Template CMake configurato con configure_file @ONLY.

Tipo variante: **adapted**. Modello di partenza: examples/#092 CMake/hello.cmake; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
cmake -DOUT=<output> -P configure.cmake; cmake -P <output>/hello.cmake
```

Risultato atteso: Hello, World!

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://cmake.org/cmake/help/latest/manual/cmake.1.html](https://cmake.org/cmake/help/latest/manual/cmake.1.html)
- [https://cmake.org/cmake/help/latest/command/message.html](https://cmake.org/cmake/help/latest/command/message.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://cmake.org/cmake/help/latest/command/configure_file.html](https://cmake.org/cmake/help/latest/command/configure_file.html)
