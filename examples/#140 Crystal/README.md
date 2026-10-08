# #140 Crystal

Voce canonica: `Crystal`, tipo `programming`, language_id `72`.

Interpolare il destinatario in una stringa Crystal, compilarla in un eseguibile nativo e stamparla.

## Toolchain e riproduzione

Crystal 1.11.2 (2024-04-01), LLVM 17.0.6, target x86_64-pc-linux-gnu.

Crystal 1.11.2 e dipendenze native GC, libevent e PCRE1. Per il pacchetto estratto impostare CRYSTAL_PATH al suo usr/lib/crystal/lib e LD_LIBRARY_PATH/LIBRARY_PATH ai prefissi locali contenenti le librerie.

Comandi dalla directory dell’esempio; `<output>` indica una directory temporanea esterna al corpus.

```text
crystal build hello.cr -o <output>/hello
<output>/hello
```

Risultato atteso: Compilazione exit 0; eseguibile exit 0, stdout esattamente Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il sorgente con interpolazione viene compilato dalla toolchain Crystal reale ed eseguito come binary Linux x86_64. Risolta la dipendenza di link libpcre3-dev con estrazione locale di pacchetti Ubuntu, senza installazione globale. Stdout e checksum del binary sono registrati.

Prova reale: [finish.json](verification/finish.json), con UTC, comandi, versioni, exit code, stdout/stderr e SHA-256 dei sorgenti. Le sostituzioni dei percorsi sono documentate nel log. I prodotti di compilazione e le dipendenze rimangono nelle directory di lavoro.

## Fonti primarie

- https://crystal-lang.org/reference/1.11/
- https://crystal-lang.org/reference/1.11/syntax_and_semantics/literals/string.html
- https://crystal-lang.org/reference/1.11/man/crystal/index.html

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.cr` | [hello.cr](hello.cr) sintassi e semantica verificate |
