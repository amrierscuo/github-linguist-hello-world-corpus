# 0085 C++ — variante `.txx`

Ruolo: Implementazione di template C++ inclusa.

Tipo variante: **adapted**. Modello di partenza: examples/#085 C++/hello.cpp; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
g++ -std=c++17 consumer.cpp -o <output>/hello; <output>/hello
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

- [https://gcc.gnu.org/onlinedocs/gcc/Standards.html](https://gcc.gnu.org/onlinedocs/gcc/Standards.html)
- [https://www.open-std.org/jtc1/sc22/wg21/](https://www.open-std.org/jtc1/sc22/wg21/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://isocpp.org/faq/templates](https://isocpp.org/faq/templates)
