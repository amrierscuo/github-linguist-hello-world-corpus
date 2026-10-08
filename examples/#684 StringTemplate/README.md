# #684 StringTemplate

Voce canonica `StringTemplate`, tipo `markup`, language_id `89855901`.

Compilare/renderizzare un template StringTemplate con parametro name.

## Toolchain e riproduzione

Official StringTemplate Java compiler/renderer ST4 4.3.4 / ANTLR runtime 3.5.3.

Occorrono Java 21, ST4 4.3.4 e ANTLR runtime 3.5.3. Il separatore classpath mostrato è quello Windows della prova; su Linux usare i due punti. Il driver Verify.java legge hello.st dalla directory corrente.

```text
java -cp "/path/ST4-4.3.4.jar;/path/antlr-runtime-3.5.3.jar" Verify.java
```

Risultato atteso: Driver ST4 exit 0; rendering World e Reader conforme. Il confronto ignora soltanto lo spazio ai bordi.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Un commento valido StringTemplate descrive il parametro name. ST4 riconosce il commento, lo elimina dal rendering e verifica nativamente sia World sia Reader con il driver Java invariato. Il commento identifica il template rispetto agli altri linguaggi .st.

Prova corrente: [recognition.json](verification/recognition.json), con UTC, comandi nativi, exit code, stdout/stderr, toolchain e SHA-256 dei sorgenti modificati e dei driver. Le prove precedenti restano come storico. L’identificazione prevista da Linguist è distinta dall’esito effettivo delle statistiche GitHub; questo lotto non applica override di linguaggio.

## Fonti primarie

- https://www.stringtemplate.org/
- https://github.com/antlr/stringtemplate4/blob/master/doc/templates.md
- https://github.com/github-linguist/linguist/blob/v9.7.0/lib/linguist/heuristics.yml

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.st` | [hello.st](hello.st) sintassi e semantica verificate |
