# #291 Harbour

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Eseguire un programma Harbour e scrivere Hello, World! su stdout.

La procedura Main crea una variabile xBase locale e usa OutStd con hb_eol. L’artefatto è sorgente Harbour, non una macro generica o un programma Bash.

## Toolchain e riproduzione

Harbour hbmk2 o hbrun originali; versioni effettive da registrare

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
hbmk2 hello.hb -ohello
```

```text
./hello oppure hbrun hello.hb
```

## Risultato atteso e stato

stdout Hello, World! seguito dall’eol della piattaforma.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compilatore/runtime nativo eseguito per questa voce.

Impedimenti: Compiler/runtime Harbour non preparati; parsing ed esecuzione pendenti.

## Fonti primarie

- https://harbour.github.io/
- https://github.com/harbour/core/blob/master/utils/hbmk2/doc/hbmk2.en.md

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.hb` | [hello.hb](hello.hb) creato, verifiche pendenti |
