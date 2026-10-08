# #535 PicoLisp

Voce canonica `PicoLisp`, tipo `programming`, language_id `285`.

Stampare il saluto con prinl e uscire dal processo PicoLisp.

## Toolchain e riproduzione

Authentic PicoLisp native interpreter 23.12-1build2.

Comando dalla directory del campione con PicoLisp 23.12-1build2. Non servono librerie esterne: de, prinl e bye sono primitive native.

```text
picolisp hello.l
```

Risultato atteso: Exit 0, stdout esattamente Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La funzione PicoLisp de greet riceve Audience e usa prinl; la chiamata greet World produce esattamente il saluto, poi bye termina il processo. La definizione de rende esplicito il dialetto e distingue .l da Lex/Common Lisp.

Prova corrente: [recognition.json](verification/recognition.json), con UTC, comandi nativi, exit code, stdout/stderr, toolchain e SHA-256 dei sorgenti modificati e dei driver. Le prove precedenti restano come storico. L’identificazione prevista da Linguist è distinta dall’esito effettivo delle statistiche GitHub; questo lotto non applica override di linguaggio.

## Fonti primarie

- https://software-lab.de/doc/refP.html#prinl
- https://software-lab.de/doc/refD.html#de
- https://github.com/github-linguist/linguist/blob/v9.7.0/lib/linguist/heuristics.yml

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.l` | [hello.l](hello.l) sintassi e semantica verificate |
