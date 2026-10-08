# #238 Genero per

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Compilare una form Genero con LABEL statica Hello, World!.

hello.per dichiara una GRID e una LABEL statica mediante item tag, identificatore e TEXT. Il goal è il contenuto della form; il file non è un programma 4GL. La verifica richiede compiler form e front-end originali.

## Toolchain e riproduzione

Genero BDL fglform e front-end compatibile; versioni effettive da registrare

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
fglform hello.per
```

```text
Aprire hello.42f con OPEN WINDOW ... WITH FORM in un programma Genero BDL.
```

## Risultato atteso e stato

La form espone la LABEL greeting_label con testo Hello, World!.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compilatore/runtime nativo eseguito per questa voce.

Impedimenti: Toolchain proprietaria Genero form e front-end non preparati; compilation/rendering pendenti.

## Fonti primarie

- https://4js.com/techdocs/fjs-fgl-manual/fgl-topics/c_fgl_FormSpecFiles_LABEL.html
- https://4js.com/online_documentation/fjs-fgl-manual-html/fgl-topics/c_fgl_FormSpecFiles_GRID.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.per` | [hello.per](hello.per) creato, verifiche pendenti |
