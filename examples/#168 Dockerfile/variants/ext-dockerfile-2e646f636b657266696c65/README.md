# 0168 Dockerfile — variante `.dockerfile`

Ruolo: Build file nel linguaggio Dockerfile; il suffisso non indica YAML/Quadlet .container.

Tipo variante: **alias**. Copia byte-identica di examples/#168 Dockerfile/Dockerfile

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
docker build -f hello.dockerfile -t corpus-greeting <contesto-temporaneo>; docker run --rm corpus-greeting
```

Risultato atteso: Parser: FROM alpine:3.22.2 e CMD exec-form corretti; runtime previsto stdout Hello, World! più newline, exit 0.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://docs.docker.com/reference/dockerfile/](https://docs.docker.com/reference/dockerfile/)
- [https://github.com/rcjsuen/dockerfile-ast](https://github.com/rcjsuen/dockerfile-ast)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
