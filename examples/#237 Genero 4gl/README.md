# #237 Genero 4gl

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Eseguire il blocco MAIN Genero 4GL e visualizzare Hello, World!.

MAIN definisce il programma, DISPLAY emette la concatenazione di stringhe mediante ||. La toolchain deve interpretare Genero 4GL; un parser SQL non verifica il blocco programma.

## Toolchain e riproduzione

Genero BDL fglcomp e fglrun; versioni effettive da registrare

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
fglcomp hello.4gl
```

```text
fglrun hello.42m
```

## Risultato atteso e stato

DISPLAY produce Hello, World! nel terminale.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compilatore/runtime nativo eseguito per questa voce.

Impedimenti: Compilatore/runtime proprietari Genero BDL non preparati; sintassi ed esecuzione pendenti.

## Fonti primarie

- https://4js.com/online_documentation/fjs-fgl-manual-html/fgl-topics/c_fgl_programs_019.html
- https://4js.com/online_documentation/fjs-fgl-manual-html/fgl-topics/c_fgl_operators_003.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.4gl` | [hello.4gl](hello.4gl) creato, verifiche pendenti |
